from fastapi import HTTPException, status
from sqlmodel import Session

from app.modules.orders.models import Pedido
from app.modules.orders.schemas import PedidoCreate, PedidoPublic
from app.modules.orders.unit_of_work import PedidoUnitOfWork


class PedidoService:

    def __init__(self, session: Session) -> None:
        self._session = session

    def create(self, data: PedidoCreate) -> PedidoPublic:
        total = sum(item.precio_snapshot * item.cantidad for item in data.items)
        pedido = Pedido(total=total, estado="pendiente")

        with PedidoUnitOfWork(self._session) as uow:
            uow.pedidos.add(pedido)
            return PedidoPublic.model_validate(pedido)

    def get_by_id(self, pedido_id: int) -> PedidoPublic:
        with PedidoUnitOfWork(self._session) as uow:
            pedido = uow.pedidos.get_by_id(pedido_id)
            if not pedido:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail="Pedido no encontrado",
                )
            pedido_pub = PedidoPublic.model_validate(pedido)
            pedido_pub.created_at = pedido.created_at.isoformat()
            return pedido_pub
