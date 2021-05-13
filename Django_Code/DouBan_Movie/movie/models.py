from django.db import models
import mongoengine
from mongoengine import ReferenceField, StringField, ListField


class MovieModel(mongoengine.Document):
    movie_url = mongoengine.StringField()
    img_url = mongoengine.StringField()
    name_chinese = mongoengine.StringField()
    name_out = mongoengine.StringField()
    score = mongoengine.StringField()
    score_num = mongoengine.StringField()
    survey = mongoengine.StringField()
    year = mongoengine.StringField()
    country = mongoengine.StringField()
    type = mongoengine.StringField()
    top = mongoengine.IntField()
    likes_num = mongoengine.IntField(required=True, default=0)  # 点赞数
    comment = mongoengine.StringField(default="暂无")  # 评论数
    # 默认都没有点赞
    click_state = mongoengine.StringField(default="glyphicon glyphicon-heart-empty")  # 点赞的状态
    # 评论
    comment_info = mongoengine.ListField()  # 存入评论


class LoginStateModel(mongoengine.Document):
    user_state = mongoengine.StringField()
