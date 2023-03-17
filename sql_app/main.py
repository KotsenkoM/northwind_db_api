from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

import crud
import models
import schemas

import database

database.Base.metadata.create_all(bind=database.engine)

app = FastAPI()


def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get('/orders/')
def read_orders(db: Session = Depends(get_db)):
    orders = crud.get_orders(db)
    return orders
