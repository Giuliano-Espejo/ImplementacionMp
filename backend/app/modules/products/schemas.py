from typing import Optional
from sqlmodel import SQLModel, Field


class ProductoPublic(SQLModel):
    id:          int
    nombre:      str
    descripcion: Optional[str] = None
    precio:      float
    imagen_url:  Optional[str] = None
