from sqlalchemy import Column, Integer, String, Date, Float, ForeignKey
from src.database import Base
from sqlalchemy.orm import relationship, Mapped, mapped_column


class Order(Base):
    __tablename__ = 'orders'

    order_id = Column('order_id', primary_key=True)
    customer_id = Column('customer_id', ForeignKey('customers.customer_id'))
    employee_id = Column('employee_id')
    order_date = Column('order_date')
    required_date = Column('required_date')
    shipped_date = Column('shipped_date')
    ship_via = Column('ship_via')
    freight = Column('freight')
    ship_name = Column('ship_name')
    ship_address = Column('ship_address')
    ship_city = Column('ship_city')
    ship_region = Column('ship_region')
    ship_postal_code = Column('ship_postal_code')
    ship_country = Column('ship_country')

    items = relationship('Customer', back_populates='owner')


class Customer(Base):
    __tablename__ = 'customers'

    customer_id = Column(String, primary_key=True)
    company_name = Column(String)
    contact_name = Column(String)
    contact_title = Column(String)
    address = Column(String)
    city = Column(String)
    region = Column(String)
    postal_code = Column(String)
    country = Column(String)
    phone = Column(String)
    fax = Column(String)

    owner = relationship('Order', back_populates='items')
