from typing import List, Optional
from sqlmodel import SQLModel, Field


class ItemPedidoCreate(SQLModel):
    producto_id:     int
    nombre_snapshot: str
    precio_snapshot: float
    cantidad:        int = Field(ge=1)


class PedidoCreate(SQLModel):
    items: List[ItemPedidoCreate]


class PedidoPublic(SQLModel):
    id:         int
    total:      float
    estado:     str
    created_at: Optional[str] = None
