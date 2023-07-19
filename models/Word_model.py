from pydantic import BaseModel


class UpdateWordAndTranslate(BaseModel):
    id_word: int
    id_translate: int
    new_word: str
    new_translate: str
