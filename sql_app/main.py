from fastapi import FastAPI
from database import get_data_from_db

app = FastAPI()


@app.get('/')
async def root():
    return {'message': 'Hello World'}


@app.get('/data')
async def read_data():
    return get_data_from_db()
