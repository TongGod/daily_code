
import mongoengine
from mongoengine import ReferenceField

from movie.models import MovieModel

class LoginModel(mongoengine.Document):
    user_name = mongoengine.StringField()
    password = mongoengine.StringField()
    img_head = mongoengine.StringField(default="static/images/default.png")
    clike_info = mongoengine.ListField(ReferenceField(MovieModel), default=[])  # 一个用户点赞可以点赞多个用户
