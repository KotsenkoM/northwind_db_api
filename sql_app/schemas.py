import datetime

from pydantic import BaseModel


class Order(BaseModel):
    customer_id: int
    employee_id: int
    order_date: datetime.date
    required_date: datetime.date
    shipped_date: datetime.date
    ship_via: int
    freight: float
    ship_name: str
    ship_address: str
    ship_city: str
    ship_region: str
    ship_postal_code: str
    ship_country: str
