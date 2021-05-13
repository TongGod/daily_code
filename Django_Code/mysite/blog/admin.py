from django.contrib import admin
from .models import Post, Comment


# Register your models here.

# 将管理站点中添加博客模型
# admin.site.register(Post)

# 使用装饰器和上述的效果相同
@admin.register(Post)
# 当前模型通过继承自ModelAdmin的自定义类在管理站点中注册
class PostAdmin(admin.ModelAdmin):
    # 设置希望在管理对象列表页面中显示的模型字段
    list_display = ('title', 'slug', 'author', 'publish', 'status')
    # 列表页面包含了右侧栏，可以设置其中的字段对结果进行过滤
    list_filter = ('status', 'created', 'publish', 'author')
    # 定义可以搜索的字段
    search_fields = ('title', 'body')
    # 自动填充字段 (输入title中的内容时候，自动填充slug的内容)
    prepopulated_fields = {'slug': ('title',)}
    # 显示外键的详细信息, 添加author时，弹出框可以选择用户
    raw_id_fields = ('author',)
    # 搜索栏下方，有导航链接，可以查看日期层次结构
    date_hierarchy = 'publish'
    # 默认状态下，帖子按照什么列进行排序
    ordering = ('status', 'publish')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'post', 'created', 'active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('name', 'email', 'body')
