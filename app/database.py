from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

DB_USER = "user"
DB_PASSWORD = ""
DB_HOST = "localhost"
DB_NAME = "ticketing"

DATABASE_URL = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"

engine_no_db = create_engine(f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/")
engine_with_db = create_engine(DATABASE_URL)

def init_database():
    if not database_exists(engine_no_db.url):
        print(f"Database '{DB_NAME}' does not exist. Creating...")
        create_database(engine_no_db.url)
    else:
        print(f"Database '{DB_NAME}' already exists.")

    from app.models import Base
    Base.metadata.create_all(bind=engine_with_db)

if __name__ == "__main__":
    init_database()