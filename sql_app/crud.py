from sqlalchemy.orm import Session

import models


def get_order(db: Session, order_id: int):
    return db.query(models.Order).filter(models.Order.order_id == order_id).first()


def get_orders(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Order).offset(skip).limit(limit).all()
