from fastapi import APIRouter, Depends
from sqlmodel import Session

from app.core.database import get_session
from app.modules.orders.schemas import PedidoCreate, PedidoPublic
from app.modules.orders.service import PedidoService

router = APIRouter(prefix="/api/v1/pedidos", tags=["pedidos"])


def get_pedido_service(session: Session = Depends(get_session)) -> PedidoService:
    return PedidoService(session)


@router.post("/", response_model=PedidoPublic, status_code=201)
def create_pedido(
    data: PedidoCreate,
    svc: PedidoService = Depends(get_pedido_service),
):
    return svc.create(data)


@router.get("/{pedido_id}", response_model=PedidoPublic)
def get_pedido(
    pedido_id: int,
    svc: PedidoService = Depends(get_pedido_service),
):
    return svc.get_by_id(pedido_id)
