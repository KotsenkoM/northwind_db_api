from sqlalchemy import Column, Integer, String, Date, Float, ForeignKey
from src.database import Base
from sqlalchemy.orm import relationship


class Order(Base):
    __tablename__ = 'orders'

    order_id = Column(Integer, primary_key=True)
    customer_id = Column(String, primary_key=True)
    employee_id = Column(Integer)
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

    # items = relationship('Customer', back_populates='owner')


# class Customer(Base):
#     __tablename__ = 'customers'
#
#     customer_id = Column(String, ForeignKey('orders.customer_id'))
#     company_name = Column(String)
#     contact_name = Column(String)
#     contact_title = Column(String)
#     address = Column(String)
#     city = Column(String)
#     region = Column(String)
#     postal_code = Column(String)
#     country = Column(String)
#     phone = Column(String)
#     fax = Column(String)
#
#     # owner = relationship('Order', back_populates='items')
