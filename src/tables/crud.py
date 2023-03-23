from sqlalchemy.orm import Session

from .models import Order, Customer


def get_orders(db: Session, limit: int = 3):
    return db.query(Order).limit(limit).all()


def get_order(db: Session, order_id: int):
    return db.query(Order).filter(Order.order_id == order_id).first()


def get_customers(db: Session, limit: int = 3):
    return db.query(Customer).limit(limit).all()


def get_customer(db: Session, customer_id: str):
    return db.query(Customer).filter(Customer.customer_id == customer_id).first()