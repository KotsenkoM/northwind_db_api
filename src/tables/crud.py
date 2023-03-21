from sqlalchemy.orm import Session

from .models import Order


def get_orders(db: Session, limit: int = 3):
    return db.query(Order).limit(limit).all()


def get_order(db: Session, order_id: int):
    return db.query(Order).filter(Order.order_id == order_id).first()
