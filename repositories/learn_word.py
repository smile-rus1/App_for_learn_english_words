from sqlalchemy import func

from data_base.models import Word, Translate
from repositories.base import BaseRepository


class LearnRepository(BaseRepository):
    def out_total_words(self, total: int) -> list[str]:
        if total == 0:
            total = 999999999

        query = [item for item in self.db.query(Word.name_word,
                                               func.ifnull(Translate.translate, "Нет перевода"))
        .outerjoin(Translate, Word.id == Translate.word_id).limit(total).all()]

        return query

    def out_random_choice_words(self, total: int):
        if total == 0:
            total = 999999999

        query = [item for item in self.db.query(Word.name_word,
                                               func.ifnull(Translate.translate, "Нет перевода"))
        .outerjoin(Translate, Word.id == Translate.word_id).order_by(func.random()).limit(total).all()]

        return query

