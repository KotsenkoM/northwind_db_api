from pydantic import BaseModel


class OrderBase(BaseModel):
    order_id: int

    class Config:
        orm_mode = True


class Order(OrderBase):
    customer_id: str


class CustomerBase(BaseModel):
    customer_id: str

    class Config:
        orm_mode = True


class Customer(CustomerBase):
    customer_id: str
