from sqlalchemy import func

from data_base.models import Word, Translate
from repositories.base import BaseRepository


class TranslateRepository(BaseRepository):
    def get_one_word(self):
        word = [item for item in self.db.query(Word.name_word).order_by(func.random()).limit(1).all()]

        yield word[0]

    def get_count_words(self, limit: int):
        words = [word for word in self.db.query(Word.name_word).order_by(func.random()).limit(limit).all()]

        yield words

    def output_translate_word(self, word: str):
        word_id = self.db.query(Word.id).filter(Word.name_word == word).first()[0]
        query = self.db.query(Translate.translate).filter(Translate.word_id == word_id).first()[0]

        yield query
