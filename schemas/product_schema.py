"""Product schema for request/response validation."""
from typing import Optional, List, TYPE_CHECKING
from pydantic import Field

from schemas.base_schema import BaseSchema

if TYPE_CHECKING:
    from schemas.category_schema import CategoryBaseSchema
    from schemas.order_detail_schema import OrderDetailBaseSchema
    from schemas.review_schema import ReviewSchema, ReviewBaseSchema


class ProductBaseSchema(BaseSchema): # Nuevo esquema ligero
    name: str = Field(..., min_length=1, max_length=200, description="Product name (required)")
    price: float = Field(..., gt=0, description="Product price (must be greater than 0, required)")
    stock: int = Field(default=0, ge=0, description="Product stock quantity (must be >= 0)")
    category_id: int = Field(..., description="Category ID reference (required)")

class ProductSchema(ProductBaseSchema): # El esquema principal hereda del base
    # La relación ahora usa el esquema base de Categoría, rompiendo el ciclo.
    category: Optional['CategoryBaseSchema'] = None
    reviews: Optional[List['ReviewBaseSchema']] = []
    order_details: Optional[List['OrderDetailBaseSchema']] = []
