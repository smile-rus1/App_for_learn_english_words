from sqlalchemy import func

from data_base.models import Translate, Word
from repositories.base import BaseRepository


class CorrectRepository(BaseRepository):
    def get_translate_word(self):
        word = [item for item in self.db.query(Translate.translate).order_by(func.random()).limit(1).all()]

        yield word[0]

    def get_quantity_translates_words(self, limit: int):
        words = [word for word in self.db.query(Translate.translate).order_by(func.random()).limit(limit).all()]

        yield words

    def output_word(self, translate: str):
        translate_entry = self.db.query(Translate).filter_by(translate=translate).first()

        yield translate_entry.word.name_word
