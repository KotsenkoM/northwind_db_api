import psycopg2
import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

load_dotenv()

SQLALCHEMY_DATABASE_URL = "postgresql://postgres:postgres@localhost/northwind"

# conn = psycopg2.connect(
#     host=os.getenv('POSTGRES_HOST'),
#     database=os.getenv('POSTGRES_DATABASE'),
#     user=os.getenv('POSTGRES_USER'),
#     password=os.getenv('POSTGRES_PASSWORD')
# )

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
