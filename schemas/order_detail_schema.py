"""OrderDetail schema with validation."""
from typing import Optional, TYPE_CHECKING
from pydantic import Field

from schemas.base_schema import BaseSchema

if TYPE_CHECKING:
    from schemas.order_schema import OrderSchemam, OrderBaseSchema
    from schemas.product_schema import ProductSchema


class OrderDetailBaseSchema(BaseSchema): # Nuevo esquema ligero
    """Esquema base de OrderDetail, sin relaciones anidadas"""
    quantity: int = Field(..., gt=0)
    price: Optional[float] = Field(None, gt=0)
    order_id: int = Field(..., description="Order ID reference (required)")
    product_id: int = Field(..., description="Product ID reference (required)")
    
# OrderDetailSchema (el principal) ahora hereda y añade las relaciones anidadas
class OrderDetailSchema(OrderDetailBaseSchema):
    # Usamos forward reference, pero el esquema anidado también debe ser ligero si tiene relaciones
    order: Optional['OrderBaseSchema'] = None
    product: Optional['ProductBaseSchema'] = None
