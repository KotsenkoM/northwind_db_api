import datetime

from pydantic import BaseModel


class OrderBase(BaseModel):
    order_id: int

    class Config:
        orm_mode = True


class Order(OrderBase):
    ship_name: str
    # customer_id: int
    # employee_id: int
    # customer_id: str
    # employee_id: int
    # order_date: datetime.date
    # required_date: datetime.date
    # shipped_date: datetime.date
    # ship_via: int
    # freight: float
    # ship_name: str
    # ship_address: str
    # ship_city: str
    # # ship_region: str
    # ship_postal_code: str
    # ship_country: str

