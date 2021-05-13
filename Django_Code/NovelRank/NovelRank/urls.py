"""NovelRank URL Configuration

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
from django.urls import path

from login.views import LoginView, UserInfoView
from novel_rank.views import HomeView, SortView, HengYanView, HengYanSortView, ChuangShiView, ChuangShiSortView
from login.views import ModifyUserView
from django.conf.urls import url
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^home/$', HomeView.as_view(), name='home'),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^sort/$', SortView.as_view(), name='sort'),
    url(r'^hengyan/$', HengYanView.as_view(), name='hengyan'),
    url(r'^hengyansort/$', HengYanSortView.as_view(), name='hengyansort'),
    url(r'^chuangshi/$', ChuangShiView.as_view(), name='chuangshi'),
    url(r'^chuangshisort/$', ChuangShiSortView.as_view(), name='chuangshisort'),
    url(r'^userinfo/$', UserInfoView.as_view(), name='userinfo'),
    url(r'^modifyuser/$', ModifyUserView.as_view(), name='modifyuser'),
]
