from sqlalchemy import create_engine, make_url
from sqlalchemy.orm import scoped_session, sessionmaker
import os

# Get environment variables
DB_DIALECT = os.getenv("DB_DIALECT", "mysql")
DB_USER = os.getenv("DB_USER", "root")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "3306")
DB_NAME = os.getenv("DB_NAME", "educacion")

DATABASE_URL = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# Create database engine
Engine = create_engine(DATABASE_URL, echo=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=Engine)


def get_db_connection():
    db = scoped_session(SessionLocal)
    print("DB connection opened")
    try:
        yield db
        print("DB connection closed")
    finally:
        db.close()
