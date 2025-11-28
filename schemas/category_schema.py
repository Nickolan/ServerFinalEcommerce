"""Category schema with validation."""
from typing import Optional, List, TYPE_CHECKING
from pydantic import Field

from schemas.base_schema import BaseSchema

#if TYPE_CHECKING:
 #   from schemas.product_schema import ProductSchema, ProductBaseSchema


class CategoryBaseSchema(BaseSchema): # Nuevo esquema ligero
    name: str = Field(..., min_length=1, max_length=100, description="Category name (required, unique)")

class CategorySchema(CategoryBaseSchema): # El esquema principal hereda del base
    # La relación ahora usa el esquema base de Producto, rompiendo el ciclo.
    products: Optional[List['ProductBaseSchema']] = []
