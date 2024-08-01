
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

# DATABASE_URL = "mysql+pymysql://user:1234@211.183.3.10/db"
DATABASE_URL = os.getenv("DB_URL","mysql+pymysql://admin:test1234@database-1.cny8owwkaw4k.ap-northeast-2.rds.amazonaws.com/db")
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()