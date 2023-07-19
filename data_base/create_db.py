import os

from data_base.base import Base, engine, db_path
from data_base.models import Word, Translate


def create_db():
    if not os.path.exists(db_path):
        os.makedirs(os.path.dirname(db_path), exist_ok=True)
        Base.metadata.create_all(engine)
