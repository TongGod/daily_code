from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset()


class Post(models.Model):
    STATUS_CHOICES = {
        ('draft', 'Draft'),
        ('published', 'Published')
    }
    # 帖子的标题字段
    title = models.CharField(max_length=250)
    # 用于URL中。slug(仅包含字母、数值、下划线以及连字符)
    # 把它设置为一个DateField或者DateTimeField的字段的名称，那么该字段的日期值就必须唯一
    slug = models.SlugField(max_length=250, unique_for_date='publish')

    # 外键，定义了多对一的关系， CASCADE：删除引用用户时，数据库还将其所关联的博客帖子
    # related_name：指定反向关系的名称
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')

    # 帖子的主体
    body = models.TextField()
    # 帖子的发布日期，以时区格式返回当前日期
    publish = models.DateTimeField(default=timezone.now)
    # 帖子的创建时间。auto_now_add（当创建某个对象时，日期将被自动保存）
    created = models.DateTimeField(auto_now_add=True)
    # 帖子的最后一个更新的时间，当保存某个对象，日期将被自动保存。
    updated = models.DateTimeField(auto_now=True)
    # 帖子的状态。choices
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

    # 添加定制管理器
    object = models.Manager()
    published = PublishedManager()

    class Meta:
        """对publish字段中的结果以降序排序"""
        ordering = ('-publish',)

    def __str__(self):
        return self.title

    # 可以使用get_absolute_url()方法，进而链接到特定的帖子
    def get_absolute_url(self):
        # reverse()方法，可通过对应的名称和所传递的可选参数构建URL
        return reverse('blog:post_detail',
                       args=[self.publish.year,
                             self.publish.month,
                             self.publish.day,
                             self.slug])


class Comment(models.Model):
    # 关联包含单一帖子的所有评论内容
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    # 通过手动的方式禁用某些不恰当的评论
    active = models.BooleanField(default=True)

    class Meta:
        # 使用created字段对 对象评论进行排序（默认状态下按照时间的排序）
        ordering = ('created',)

    def __str__(self):
        return 'Comment by {} on {}'.format(self.name, self.post)
