from peewee import *

db = SqliteDatabase('server.db')

class BaseModel(Model):
    id = PrimaryKeyField(unique=True)
    class Meta:
        database = db
        order_by = 'id'

class User(BaseModel):
    login = CharField()
    password = CharField()
    class Meta:
        db_table = 'users'

class Post(BaseModel):
    expense_id = ForeignKeyField(User)
    text = CharField()
    class Meta:
        db_table = 'posts'

class BasePost(BaseModel):
    expense_id = ForeignKeyField(Post)

class Image(BasePost):
    photo = BlobField()
    class Meta:
        db_table = 'images'

class Like(BasePost):
    userLike = CharField()
    class Meta:
        db_table = 'likes'

class Sub(BaseModel):
    expense_id = ForeignKeyField(User)
    loginSub = CharField()
    class Meta:
        db_table = 'subs'

with db:
    db.create_tables([User, Post, Sub, Like, Image])