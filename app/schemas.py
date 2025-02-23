from pydantic import BaseModel

class OrderCreate(BaseModel):
    symbol: str
    price: float
    quantity: int
    order_type: str

class OrderOut(BaseModel):
    id: int
    symbol: str
    price: float
    quantity: int
    order_type: str

    class Config:
        orm_mode = True