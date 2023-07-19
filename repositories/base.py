from abc import ABC

from sqlalchemy.orm import Session

from data_base.base import get_db


class BaseRepository(ABC):
    def __init__(self):
        self.db: Session = next(get_db())

    # @abstractmethod
    # def get_all(self):
    #     ...
    #
    # @abstractmethod
    # def add_word_and_translate(self, *args):
    #     ...
    #
    # @abstractmethod
    # def delete_from_db(self, *args):
    #     ...
    #
    # @abstractmethod
    # def update_words_translate(self, *args):
    #     ...
