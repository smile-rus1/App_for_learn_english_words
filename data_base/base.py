import os

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker


BASE_DIR = os.path.dirname(os.path.abspath(__name__))

db_path = "DB/learn_words.sqlite"

Base = declarative_base()

engine = create_engine(f"sqlite:///{db_path}", connect_args={"check_same_thread": False}, echo=True)

Session = sessionmaker(bind=engine, autoflush=False, autocommit=False)


def get_db():
    db = Session()
    try:
        yield db

    finally:
        db.close()
