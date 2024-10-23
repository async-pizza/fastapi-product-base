from pydantic import BaseModel


class DBSchema(BaseModel):
    id: int


class ProductInSchema(BaseModel):
    name: str
    description: str | None = None
    price: float
    stock_quantity: int
    category_id: int


class ProductSchema(ProductInSchema, DBSchema):
    pass


class CategoryInSchema(BaseModel):
    name: str


class CategorySchema(CategoryInSchema, DBSchema):
    pass
