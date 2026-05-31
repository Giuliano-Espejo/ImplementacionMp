from sqlmodel import Session
from app.core.base_repository import BaseRepository
from app.modules.orders.models import Pedido


class PedidoRepository(BaseRepository[Pedido]):

    def __init__(self, session: Session):
        super().__init__(Pedido, session)
