from django.db import models


# Create your models here.


class GameInfo(models.Model):
    """游戏模型类"""

    title = models.CharField(max_length=200, null=True)
    type = models.CharField(max_length=100, null=True)
    rating = models.CharField(max_length=200, null=True)
    platforms = models.CharField(max_length=200, null=True)
    n_ratings = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.title

    class Meta:
        # 对应数据库中的表名
        db_table = 'douban_game'
