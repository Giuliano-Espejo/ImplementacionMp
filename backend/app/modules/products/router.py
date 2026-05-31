from fastapi import APIRouter, Depends
from sqlmodel import Session

from app.core.database import get_session
from app.modules.products.schemas import ProductoPublic
from app.modules.products.service import ProductoService

router = APIRouter(prefix="/api/v1/productos", tags=["productos"])


def get_producto_service(session: Session = Depends(get_session)) -> ProductoService:
    return ProductoService(session)


@router.get("", response_model=list[ProductoPublic])
def list_productos(
    svc: ProductoService = Depends(get_producto_service),
):
    return svc.list_all()


@router.get("/{producto_id}", response_model=ProductoPublic)
def get_producto(
    producto_id: int,
    svc: ProductoService = Depends(get_producto_service),
):
    return svc.get_by_id(producto_id)
