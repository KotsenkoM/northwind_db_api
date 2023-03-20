from sqlalchemy.orm import Session

from .models import Order


def get_orders(db: Session, limit: int = 5):
    return db.query(Order).limit(limit).all()


def get_order(db: Session, order_id: int):
    return db.query(Order).offset(order_id)
