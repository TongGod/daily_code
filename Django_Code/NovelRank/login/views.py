from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic.base import View
from login.models import LoginModel, LoginStateModel


# 注册登录功能
class LoginView(View):
    def get(self, request):
        return render(request, "login.html")

    def post(self, request):
        if "login" in request.POST:
            user = request.POST.get("user_login")
            pwd = request.POST.get("pwd_login")
            login_info = LoginModel.objects.filter(username=user, password=pwd)
            if len(login_info) != 0:
                rep = redirect("/home/")
                # 设置一个加密的cookie,默认值为"1"，加密条件"already_login"
                rep.set_signed_cookie("is_login", "1", salt="already_login")
                # 存入正在登陆的用户名
                LoginStateModel(login_state=user).save()
                return rep
            else:
                flag = True
                return render(request, 'login.html', {"flag": flag, 'success': False})
        if "register" in request.POST:
            user_name = request.POST.get("user")
            password = request.POST.get("pwd")
            if user_name != "" and password != "":
                login_name = LoginModel.objects.filter(username=user_name)
                login_pwd = LoginModel.objects.filter(password=password)
                if len(login_name) == 0 and len(login_pwd) == 0:
                    logininfo = LoginModel(username=user_name, password=password)
                    logininfo.save()
                    return render(request, 'login.html', {'success': True, "flag": False})
                else:
                    return render(request, 'login.html', {'already_exis': True, "flag": False})
            else:
                return render(request, 'login.html', {"flag": False, "re_em": True})


# 个人中心
class UserInfoView(View):
    def get(self, request):
        username = LoginStateModel.objects.all()[0].login_state  # 获取到当前登录的用户名
        password = LoginModel.objects.filter(username=username)[0].password  # 获取当前登录的密码

        # 获取该用户的头像的路径
        login_user = LoginModel.objects.filter(username=username)[0]
        img_head = login_user.img_head
        data = {
            "username": username,
            "password": password,
            "img_head": img_head
        }

        return render(request, 'user_info.html', context=data)


# 个人中心修改资料以及删除评论
class ModifyUserView(View):
    def post(self, request):
        name = request.POST.get("name")  # 获取到要修改的用户名
        pwd = request.POST.get("pwd")  # 获取到要修改的密码
        username = LoginStateModel.objects.all()[0].login_state  # 获取到当前登录的用户名
        if len(name) != 0 and len(pwd) != 0:

            # 修改用户名 和 密码
            modify_name = LoginModel.objects.get(username=username)
            modify_name.username = name
            modify_name.password = pwd
            modify_name.save()

            # 修改登录状态的用户名
            login_state = LoginStateModel.objects.get(login_state=username)
            login_state.login_state = name
            login_state.save()

            # 修改 该用户名评论的电影的用户名数据
            img = request.FILES.get("face")
            if img is not None:
                path = default_storage.save("static/images/" + username + ".png", ContentFile(img.read()))
                login_user = LoginModel.objects.get(username=name)
                login_user.img_head = path
                login_user.save()

            return redirect('userinfo')
        if len(name) == 0 and len(pwd) != 0:
            modify_name = LoginModel.objects.get(username=username)
            modify_name.password = pwd
            modify_name.save()

            img = request.FILES.get("face")
            if img is not None:
                path = default_storage.save("static/images/" + username + ".png", ContentFile(img.read()))
                login_user = LoginModel.objects.get(username=name)
                login_user.img_head = path
                login_user.save()
            return redirect('userinfo')
        if len(name) != 0 and len(pwd) == 0:
            # 修改登录状态用户名
            login_state_name = LoginStateModel.objects.get(login_state=username)
            login_state_name.login_state = name
            login_state_name.save()

            # 修改用户名
            modify_name = LoginModel.objects.get(username=username)
            modify_name.username = name
            modify_name.save()

            img = request.FILES.get("face")
            if img is not None:
                path = default_storage.save("static/images/" + username + ".png", ContentFile(img.read()))

                login_user = LoginModel.objects.get(username=username)
                login_user.img_head = path
                login_user.save()
            return redirect('userinfo')
        if len(name) == 0 and len(pwd) == 0:
            img = request.FILES.get("face")
            if img is not None:
                path = default_storage.save("static/images/" + username + ".png", ContentFile(img.read()))
                login_user = LoginModel.objects.get(username=username)
                login_user.img_head = path
                login_user.save()
            return redirect('userinfo')
