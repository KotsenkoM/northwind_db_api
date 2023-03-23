from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from .tables import crud, models, schemas
from .database import Base, engine, SessionLocal

Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get('/orders/', response_model=list[schemas.OrderBase])
def read_orders(db: Session = Depends(get_db)):
    '''Отобразить все заказы'''
    orders = crud.get_orders(db)
    return orders


@app.get('/orders/{order_id}', response_model=schemas.Order)
def read_order(order_id: int, db: Session = Depends(get_db)):
    db_order = crud.get_order(db, order_id=order_id)
    if db_order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    return db_order


@app.get('/customers/', response_model=list[schemas.CustomerBase])
def read_orders(db: Session = Depends(get_db)):
    customers = crud.get_customers(db)
    return customers


@app.get('/customers/{customer_id}', response_model=schemas.Customer)
def read_order(customer_id: str, db: Session = Depends(get_db)):
    db_customer = crud.get_customer(db, customer_id=customer_id)
    if db_customer is None:
        raise HTTPException(status_code=404, detail="Customer not found")
    return db_customer
