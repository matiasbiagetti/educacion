from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

DATABASE_URL = f"{DB_DIALECT}://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# Create database engine
Engine = create_engine(DATABASE_URL, echo=True, pool_size=20, max_overflow=10, pool_recycle=60*5, pool_pre_ping=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=Engine)

def get_db_connection():
    db = scoped_session(SessionLocal)
    try:
        yield db
    finally:
        db.close()
