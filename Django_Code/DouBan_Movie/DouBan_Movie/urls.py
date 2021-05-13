"""DouBan_Movie URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from movie.views import HomeView, SearchView, StaInfoView, UserInfoView, ClickCommentView, CommentInfoView , HomePageView , ModifyUserView
from login.views import LoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', HomePageView.as_view(), name='homepage'),
    url(r'^home/(?P<username>[-\w]+)/', HomeView.as_view(), name='home'),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^search/(?P<username>[-\w]+)/$', SearchView.as_view(), name='search'),
    url(r'^draw/$', StaInfoView.as_view(), name='draw'),
    url(r'^user/$', UserInfoView.as_view(), name='user'),
    url(r'^clickcomment/$', ClickCommentView.as_view(), name='clickcomment'),
    url(r'^commentinfo/$', CommentInfoView.as_view(), name='commentinfo'),
    url(r'^modifyuser/$', ModifyUserView.as_view(), name='modifyuser')
]
