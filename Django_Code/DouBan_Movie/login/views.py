from django.contrib import auth
from django.contrib.auth import login
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse
from django.views.generic.base import View
from login.models import LoginModel


# 注册登录功能
class LoginView(View):
    def get(self, request):
        return render(request, "login.html")

    def post(self, request):
        if "login" in request.POST:
            user = request.POST.get("user_login")
            pwd = request.POST.get("pwd_login")
            login_info = LoginModel.objects.filter(user_name=user, password=pwd)
            if len(login_info) != 0:  # "/home/"
                rep = redirect(reverse("home", kwargs={"username": user}))
                # 设置一个加密的cookie,默认值为"1"，加密条件"already_login"
                rep.set_signed_cookie("is_login", "1", salt="already_login")
                return rep
            else:
                flag = True
                return render(request, 'login.html', {"flag": flag, 'success': False})
        if "register" in request.POST:
            user_name = request.POST.get("user")
            password = request.POST.get("pwd")
            if user_name != "" and password != "":
                login_name = LoginModel.objects.filter(user_name=user_name)
                login_pwd = LoginModel.objects.filter(password=password)
                if len(login_name) == 0 and len(login_pwd) == 0:
                    logininfo = LoginModel(user_name=user_name, password=password)
                    logininfo.save()
                    return render(request, 'login.html', {'success': True, "flag": False})
                else:
                    return render(request, 'login.html', {'already_exis': True, "flag": False})
            else:
                return render(request, 'login.html', {"flag": False, "re_em": True})
