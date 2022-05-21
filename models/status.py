from peewee import *
from .base import BaseModel
from playhouse.shortcuts import model_to_dict


class Status(BaseModel):
    id = PrimaryKeyField(null=False)
    ru = CharField(max_length=25)
    en = CharField(max_length=25)

    class Meta:
        db_table = "status"


def list_status(code: str):
    status_list = list(Status.select())
    status_list = [model_to_dict(language) for language in status_list]
    for language in status_list:
        if code == 'ru':
            language['name'] = language['ru']
        elif code == 'en':
            language['name'] = language['en']
        else:
            language['name'] = language['en']
    return status_list
