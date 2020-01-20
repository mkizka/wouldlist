from typing import Tuple

from tortoise import fields, models

from app.utils import SerializableMixin


class User(SerializableMixin, models.Model):
    uid = fields.CharField(pk=True, max_length=50)

    name = fields.CharField(max_length=50)
    screen_name = fields.CharField(max_length=20)
    photo_url = fields.CharField(max_length=255)

    def get_serialize_fields(self) -> Tuple[str, ...]:
        return 'name', 'photo_url', 'screen_name'

    def __str__(self) -> str:
        return f'{self.name}(@{self.screen_name})'


class Item(SerializableMixin, models.Model):
    uid = fields.UUIDField(pk=True)
    user = fields.ForeignKeyField('models.User')
    text = fields.CharField(max_length=200)

    def get_serialize_fields(self) -> Tuple[str, ...]:
        return 'id', 'title', 'text'
