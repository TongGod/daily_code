from django.shortcuts import render, get_object_or_404
from .models import Post, Comment
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView
from .forms import EmailPostForm, CommentForm


# Create your views here.


# 显示帖子列表
def post_list(request):
    object_list = Post.published.all()
    paginator = Paginator(object_list, 3)  # 每个页面显示三个
    # 获取表示当前页面号的pageGET参数
    page = request.GET.get('page')
    try:
        # 获得所需页面的对象
        posts = paginator.page(page)
    except PageNotAnInteger:
        # 如果页面不是整数，则传递第一页
        posts = paginator.page(1)
    except EmptyPage:
        # 如果页面超出范围，则提供结果的最后一页
        posts = paginator.page(paginator.num_pages)
    return render(request, 'blog/post/list.html', {'page': page, 'posts': posts})


# 显示独立的帖子
def post_detail(request, year, month, day, post):
    # get_object_or_404:对象不存在抛HTTP404
    post = get_object_or_404(
        Post, slug=post, publish__year=year,
        publish__month=month, publish__day=day
    )

    # 此帖子的活动评论列表，对该帖子进行检索评论
    comments = post.comments.filter(active=True)

    # 让相同的视图以使用户能够添加新的评论
    new_comment = None

    if request.method == 'POST':
        # 发表了一条评论，采用提交的数据对表单实例化
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            # 创建评论对象，但不保存到数据库
            # save() 方法创建表单所链接的模型实例，并将其保存至数据库中。
            new_comment = comment_form.save(commit=False)
            # 分配当前帖子给评论，（将当前帖子置于刚刚创建的评论）
            new_comment.post = post
            # 保存这些评论到数据库（将最新的评论保存至数据库中）
            new_comment.save()
    else:
        comment_form = CommentForm()
    print('*'*30)
    print(comment_form)
    return render(request, 'blog/post/detail.html',
                  {'post': post, 'comments': comments,
                   'new_comment': new_comment,
                   'comment_form': comment_form})


# 当提交成功后，将发送一封电子邮件
def post_share(request, post_id):
    # 按id检索帖子，以确保检索的帖子包含 published
    post = get_object_or_404(Post, id=post_id, status='published')
    # 如果获得一个POST请求，将表单提交并且处理
    if request.method == 'POST':
        # 通过包含于request.POST中的提交数据生成一个表单实例
        form = EmailPostForm(request.POST)
        # 利用表单的is_valid()端点验证所提交的数据。该方法对表单中引入的数据进行验证
        # 若全部字段均为包含有效数据，则返回True。否则返回False
        if form.is_valid():
            # 表单已通过验证，通过访问cleaned_data将对验证后的数据进行检索
            # 该属性表示为表单字段及其对应值的字典
            cd = form.cleaned_data
            # ...发送email
    else:
        # 如果获得GET请求时，显示一个空表单
        form = EmailPostForm()
    return render(request, 'blog/post/share.html', {'post': post, 'form': form})


class PostListView(ListView):
    queryset = Post.published.all()
    content_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog/post/list.html'
    # 传递到前段的对象名称为  page_obj
