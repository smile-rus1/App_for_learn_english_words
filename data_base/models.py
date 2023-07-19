from sqlalchemy import Column, INTEGER, VARCHAR, ForeignKey
from sqlalchemy.orm import relationship

from data_base.base import Base


class Word(Base):
    __tablename__ = "words"

    id = Column(INTEGER, primary_key=True, nullable=False, autoincrement=True)
    name_word = Column(VARCHAR(50), nullable=False)

    translates = relationship("Translate", cascade="all, delete", backref="word")


class Translate(Base):
    __tablename__ = "translates"

    id = Column(INTEGER, primary_key=True, nullable=False, autoincrement=True)
    translate = Column(VARCHAR(100), nullable=False)

    word_id = Column(INTEGER, ForeignKey("words.id", ondelete="CASCADE"))
