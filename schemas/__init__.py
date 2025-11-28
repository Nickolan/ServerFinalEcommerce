from schemas.address_schema import AddressSchema
from schemas.bill_schema import BillSchema
from schemas.client_schema import ClientSchema
from schemas.order_detail_schema import OrderDetailBaseSchema, OrderDetailSchema
from schemas.order_schema import OrderSchema, OrderBaseSchema
from schemas.review_schema import ReviewBaseSchema, ReviewSchema
from schemas.product_schema import ProductBaseSchema, ProductSchema
from schemas.category_schema import CategoryBaseSchema, CategorySchema

AddressSchema.model_rebuild()
ClientSchema.model_rebuild()
OrderSchema.model_rebuild()
OrderBaseSchema.model_rebuild()
OrderDetailSchema.model_rebuild()
OrderDetailBaseSchema.model_rebuild()
ReviewSchema.model_rebuild()
ReviewBaseSchema.model_rebuild()
BillSchema.model_rebuild()
ProductBaseSchema.model_rebuild() 
CategoryBaseSchema.model_rebuild()
ProductSchema.model_rebuild() 
CategorySchema.model_rebuild()
