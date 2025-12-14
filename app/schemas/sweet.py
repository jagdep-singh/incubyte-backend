from pydantic import BaseModel


class SweetCreate(BaseModel):
    name: str
    category: str
    price: float
    quantity: int


class SweetOut(SweetCreate):
    id: int
