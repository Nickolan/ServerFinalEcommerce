from typing import Optional, TYPE_CHECKING
from pydantic import Field

from schemas.base_schema import BaseSchema

if TYPE_CHECKING:
    from schemas.product_schema import ProductBaseSchema


class ReviewBaseSchema(BaseSchema): # <-- NUEVO: Esquema Base
    """Esquema base de Review, sin la relación anidada de Producto."""
    rating: float = Field(..., ge=1.0, le=5.0)
    comment: Optional[str] = Field(None, min_length=10, max_length=1000)
    product_id: int = Field(..., description="Product ID reference (required)")
    # Nota: client_id no está en el modelo, lo omitimos para mantener coherencia.

# El esquema principal ahora hereda del base y añade la relación anidada:
class ReviewSchema(ReviewBaseSchema): # <-- CAMBIO: Hereda del Base
    product: Optional['ProductBaseSchema'] = None #
