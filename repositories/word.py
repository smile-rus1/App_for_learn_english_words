from sqlalchemy import func

from repositories.base import BaseRepository

from data_base.models import Word, Translate


class WordRepository(BaseRepository):
    def get_all(self) -> list[str]:
        query = [item for item in self.db.query(Word.id, Word.name_word,
                                                func.ifnull(Translate.translate, "Нет перевода"))
        .outerjoin(Translate, Word.id == Translate.word_id).all()
                 ]

        return query

    def add_word_and_translate(self, word: str, translate: str):
        try:
            if word is None:
                return

            add_word = Word(name_word=word)
            self.db.add(add_word)
            self.db.commit()

            id_word = self.db.query(Word.id).filter(Word.name_word == word).first()[0]
            add_translate = Translate(translate=translate, word_id=id_word)

            self.db.add(add_translate)
            self.db.commit()

        except Exception as ex:
            self.db.rollback()
            raise ValueError("Неправильно переданы аргументы!")

    def delete_from_db(self, name: str):
        id_word = self.db.query(Word.id).filter(Word.name_word == name).first()[0]
        delete_word = self.db.query(Word).filter_by(id=id_word).first()

        self.db.delete(delete_word)
        self.db.commit()

    def update_words_translate(self, id_word: int, name_word: str, name_translate: str):
        word = self.db.query(Word).filter_by(id=id_word).first()
        word.name_word = name_word
        print(name_translate)

        translate_id = self.db.query(Translate.id).filter(Translate.word_id == id_word).first()[0]
        translate = self.db.query(Translate).filter_by(id=translate_id).first()
        translate.translate = name_translate

        self.db.commit()

    # def check_in_db(self, value: str):  # додумать как реализовать функцию
    #     in_db = self.db.query(exists().where(Word.name_word == value))
    #
    #     if in_db:
    #         return False
    #
    #     return True
