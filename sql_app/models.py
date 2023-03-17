from sqlalchemy import Column, Integer, String, Date, Float
import database


class Order(database.Base):
    __tablename__ = 'orders'

    order_id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(Integer, index=True)
    employee_id = Column(Integer, index=True)
    order_date = Column(Date)
    required_date = Column(Date)
    shipped_date = Column(Date)
    ship_via = Column(Integer)
    freight = Column(Float)
    ship_name = Column(String)
    ship_address = Column(String)
    ship_city = Column(String)
    ship_region = Column(String)
    ship_postal_code = Column(String)
    ship_country = Column(String)
