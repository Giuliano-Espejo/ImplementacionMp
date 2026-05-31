from sqlmodel import Session, select

from app.core.base_repository import BaseRepository
from app.modules.products.models import Producto


class ProductoRepository(BaseRepository[Producto]):

    def __init__(self, session: Session):
        super().__init__(Producto, session)

    def get_activos(self) -> list[Producto]:
        return list(
            self.session.exec(
                select(Producto).where(Producto.activo == True)
            ).all()
        )
