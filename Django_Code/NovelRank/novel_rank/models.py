from django.db import models


# Create your models here.
class ZongHengModel(models.Model):
    """纵横小说网模型类"""
    top = models.IntegerField(null=True)
    bookname = models.CharField(max_length=150, null=True)
    info = models.CharField(max_length=500, null=True)
    click = models.IntegerField(null=True)
    label = models.CharField(max_length=200, null=True)
    type = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.bookname

    class Meta:
        # 对应数据库中的表名
        db_table = 'zongheng'
        ordering = ['id']


class HengYanModel(models.Model):
    """恒言小说网模型类"""
    top = models.IntegerField(null=True)
    bookname = models.CharField(max_length=150, null=True)
    click = models.IntegerField(null=True)
    info = models.CharField(max_length=500, null=True)
    label = models.CharField(max_length=200, null=True)
    type = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.bookname

    class Meta:
        # 对应数据库中的表名
        db_table = 'hengyan'
        ordering = ['id']

class ChuangShiModel(models.Model):
    """创世小说网模型类"""
    top = models.IntegerField(null=True)
    bookname = models.CharField(max_length=150, null=True)
    collection = models.IntegerField(null=True)
    info = models.CharField(max_length=500, null=True)
    label = models.CharField(max_length=200, null=True)
    type = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.bookname

    class Meta:
        # 对应数据库中的表名
        db_table = 'chuangshi'
        ordering = ['id']
