from peewee import *
from .base import BaseModel


class Vocabulary(BaseModel):
    id = PrimaryKeyField(null=False)
    code = CharField(max_length=2)
    name = CharField()
    value = CharField()

    class Meta:
        db_table = "vocabulary"


async def get_labels(code: str):
    return {lng.name: lng.value for lng in Vocabulary.select().filter(Vocabulary.code == code)}
