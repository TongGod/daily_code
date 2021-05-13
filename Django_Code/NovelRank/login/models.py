from django.db import models


# Create your models here.
class LoginModel(models.Model):
    username = models.CharField(max_length=100, null=True)
    password = models.CharField(max_length=100, null=True)
    img_head = models.CharField(max_length=200, default="static/images/default.jpg")

    def __str__(self):
        return self.username

    class Meta:
        # 对应数据库中的表名
        db_table = 'login'


class LoginStateModel(models.Model):
    login_state = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.login_state

    class Meta:
        # 对应数据库中的表名
        db_table = 'login_state'
