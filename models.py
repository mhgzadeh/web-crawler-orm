from datetime import datetime
from peewee import SqliteDatabase, Model, CharField, TextField, BooleanField, \
    DateTimeField, ForeignKeyField

db = SqliteDatabase('Post.db')


class BaseModel(Model):
    create_time = DateTimeField(default=datetime.now())

    class Meta:
        database = db


class Category(BaseModel):
    name = CharField()


class Article(BaseModel):
    url = CharField()

    title = CharField(null=True)
    body = TextField(null=True)
    is_completed = BooleanField(default=False)

    category = ForeignKeyField(Category, backref='articles')
