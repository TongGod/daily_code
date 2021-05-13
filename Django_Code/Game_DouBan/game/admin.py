from django.contrib import admin

from game.models import GameInfo
# 后台管理相关文件
# Register your models here.
# 注册模型类
admin.site.register(GameInfo) # 进行注册
