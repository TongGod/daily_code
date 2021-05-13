from django.contrib.auth import logout
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View

from login.models import LoginStateModel, LoginModel
from .models import ZongHengModel, HengYanModel, ChuangShiModel
import re
from novel_rank.pager_tool import get_pager


class HomeView(View):
    def get(self, request):
        ret = request.get_signed_cookie("is_login", default="0", salt="already_login")
        if ret == "1":  # 如果为1，代表已经登陆成功
            if request.GET.get("state") == "false":
                logout(request)
                # 退出登录，重定向到登录页
                response = redirect("/login/")
                # 退出登录时清除cookie中的is_login
                response.delete_cookie("is_login")
                LoginStateModel.objects.all().delete()
                return response
            else:
                zongheng = ZongHengModel.objects.all()
                for zh in zongheng:
                    for i in range(0, len(zh.info), 30):
                        zh.info = zh.info[:i] + "<p>" + zh.info[i:] + "</p>"
                data = get_pager(zongheng, request)[0]
                username = LoginStateModel.objects.all()[0].login_state
                login_user = LoginModel.objects.filter(username=username)[0]
                img_head = login_user.img_head
                return render(request, 'zongheng.html', context={
                    'data': data, "zongheng": get_pager(zongheng, request)[1],
                    "click_state1": "active", "username": username, "img_head": img_head
                })
        else:
            return redirect("/login/")


class SortView(View):

    def get(self, request):
        username = LoginStateModel.objects.all()[0].login_state
        login_user = LoginModel.objects.filter(username=username)[0]
        img_head = login_user.img_head
        if request.GET.get("sort") == "one_sort":
            if request.GET.get("order") == "min_max":  # 从小到大
                zongheng = ZongHengModel.objects.order_by('click')  # 升序
                state1 = "success"
                state2 = "text"
                order = "min_max"
            else:
                zongheng = ZongHengModel.objects.order_by('-click')  # 降序
                state1 = "text"
                state2 = "success"
                order = "max_min"
            one_sort = []
            for zh in zongheng:
                if zh.type == "奇幻·玄幻":
                    one_sort.append(zh)
            for zh in one_sort:
                for i in range(0, len(zh.info), 30):
                    zh.info = zh.info[:i] + "<p>" + zh.info[i:] + "</p>"
            data = get_pager(one_sort, request)[0]

            return render(request, 'zongheng.html', context={
                'data': data, "zongheng": get_pager(one_sort, request)[1],
                "one_state": "success",
                'sort': "one_sort",
                "state1": state1,
                "state2": state2,
                "order": order,
                "click_state1": "active",
                "username": username,
                "img_head": img_head
            })
        elif request.GET.get("sort") == "two_sort":
            if request.GET.get("order") == "min_max":  # 从小到大
                zongheng = ZongHengModel.objects.order_by('click')  # 升序
                state1 = "success"
                state2 = "text"
                order = "min_max"
            else:
                zongheng = ZongHengModel.objects.order_by('-click')  # 降序
                state1 = "text"
                state2 = "success"
                order = "max_min"
            two_sort = []
            for zh in zongheng:
                if zh.type == "都市·娱乐":
                    two_sort.append(zh)
            for zh in two_sort:
                for i in range(0, len(zh.info), 30):
                    zh.info = zh.info[:i] + "<p>" + zh.info[i:] + "</p>"
            data = get_pager(two_sort, request)[0]
            return render(request, 'zongheng.html', context={
                'data': data, "zongheng": get_pager(two_sort, request)[1],
                "two_state": "success",
                'sort': "two_sort",
                "state1": state1,
                "state2": state2,
                "order": order,
                "click_state1": "active",
                "username": username,
                "img_head": img_head
            })
        elif request.GET.get("sort") == "all_sort":
            if request.GET.get("order") == "min_max":  # 从小到大
                zongheng = ZongHengModel.objects.order_by('click')  # 升序
                state1 = "success"
                state2 = "text"
                order = "min_max"
            else:
                zongheng = ZongHengModel.objects.order_by('-click')  # 降序
                state1 = "text"
                state2 = "success"
                order = "max_min"
            for zh in zongheng:
                for i in range(0, len(zh.info), 30):
                    zh.info = zh.info[:i] + "<p>" + zh.info[i:] + "</p>"
            data = get_pager(zongheng, request)[0]
            return render(request, 'zongheng.html', context={
                'data': data, "zongheng": get_pager(zongheng, request)[1],
                "all_state": "success",
                'sort': "all_sort",
                "state1": state1,
                "state2": state2,
                "order": order,
                "click_state1": "active",
                "username": username,
                "img_head": img_head
            })
        else:
            if request.GET.get("order") == "min_max":  # 从小到大
                zongheng = ZongHengModel.objects.order_by('click')  # 升序
                state1 = "success"
                state2 = "text"
                order = "min_max"
            else:
                zongheng = ZongHengModel.objects.order_by('-click')  # 降序
                state1 = "text"
                state2 = "success"
                order = "max_min"
            three_sort = []
            for zh in zongheng:
                if zh.type == "都市·娱乐":
                    three_sort.append(zh)
            for zh in three_sort:
                for i in range(0, len(zh.info), 30):
                    zh.info = zh.info[:i] + "<p>" + zh.info[i:] + "</p>"
            data = get_pager(three_sort, request)[0]
            return render(request, 'zongheng.html', context={
                'data': data, "zongheng": get_pager(three_sort, request)[1],
                "three_state": "success",
                'sort': "three_sort",
                "state1": state1,
                "state2": state2,
                "order": order,
                "click_state1": "active",
                "username": username,
                "img_head": img_head
            })


class HengYanView(View):
    def get(self, request):
        ret = request.get_signed_cookie("is_login", default="0", salt="already_login")
        username = LoginStateModel.objects.all()[0].login_state
        login_user = LoginModel.objects.filter(username=username)[0]
        img_head = login_user.img_head
        if ret == "1":  # 如果为1，代表已经登陆成功
            if request.GET.get("state") == "false":
                logout(request)
                # 退出登录，重定向到登录页
                response = redirect("/login/")
                # 退出登录时清除cookie中的is_login
                response.delete_cookie('is_login')
                return redirect("/login/")
            else:
                hengyan = HengYanModel.objects.all()
                for zh in hengyan:
                    for i in range(0, len(zh.info), 30):
                        zh.info = zh.info[:i] + "<p>" + zh.info[i:] + "</p>"
                data = get_pager(hengyan, request)[0]
                return render(request, 'hengyan.html', context={
                    'data': data, "hengyan": get_pager(hengyan, request)[1],
                    "click_state2": "active", "username": username, "img_head": img_head
                })
        else:
            return redirect("/login/")


class HengYanSortView(View):

    def get(self, request):
        username = LoginStateModel.objects.all()[0].login_state
        login_user = LoginModel.objects.filter(username=username)[0]
        img_head = login_user.img_head
        if request.GET.get("sort") == "one_sort":
            if request.GET.get("order") == "min_max":  # 从小到大
                hengyan = HengYanModel.objects.order_by('click')  # 升序
                state1 = "success"
                state2 = "text"
                order = "min_max"
            else:
                hengyan = HengYanModel.objects.order_by('-click')  # 降序
                state1 = "text"
                state2 = "success"
                order = "max_min"
            one_sort = []
            for zh in hengyan:
                if zh.type == "玄幻":
                    one_sort.append(zh)
            for zh in one_sort:
                for i in range(0, len(zh.info), 30):
                    zh.info = zh.info[:i] + "<p>" + zh.info[i:] + "</p>"
            data = get_pager(one_sort, request)[0]
            return render(request, 'hengyan.html', context={
                'data': data, "hengyan": get_pager(one_sort, request)[1],
                "one_state": "success",
                'sort': "one_sort",
                "state1": state1,
                "state2": state2,
                "order": order,
                "click_state2": "active",
                "username": username,
                "img_head": img_head
            })
        elif request.GET.get("sort") == "two_sort":
            if request.GET.get("order") == "min_max":  # 从小到大
                hengyan = HengYanModel.objects.order_by('click')  # 升序
                state1 = "success"
                state2 = "text"
                order = "min_max"
            else:
                hengyan = HengYanModel.objects.order_by('-click')  # 降序
                state1 = "text"
                state2 = "success"
                order = "max_min"
            two_sort = []
            for zh in hengyan:
                if zh.type == "言情":
                    two_sort.append(zh)
            for zh in two_sort:
                for i in range(0, len(zh.info), 30):
                    zh.info = zh.info[:i] + "<p>" + zh.info[i:] + "</p>"
            data = get_pager(two_sort, request)[0]
            return render(request, 'hengyan.html', context={
                'data': data, "hengyan": get_pager(two_sort, request)[1],
                "two_state": "success",
                'sort': "two_sort",
                "state1": state1,
                "state2": state2,
                "order": order,
                "click_state2": "active",
                "username": username,
                "img_head": img_head
            })
        elif request.GET.get("sort") == "all_sort":
            if request.GET.get("order") == "min_max":  # 从小到大
                hengyan = HengYanModel.objects.order_by('click')  # 升序
                state1 = "success"
                state2 = "text"
                order = "min_max"
            else:
                hengyan = HengYanModel.objects.order_by('-click')  # 降序
                state1 = "text"
                state2 = "success"
                order = "max_min"
            for zh in hengyan:
                for i in range(0, len(zh.info), 30):
                    zh.info = zh.info[:i] + "<p>" + zh.info[i:] + "</p>"
            data = get_pager(hengyan, request)[0]
            return render(request, 'hengyan.html', context={
                'data': data, "hengyan": get_pager(hengyan, request)[1],
                "all_state": "success",
                'sort': "all_sort",
                "state1": state1,
                "state2": state2,
                "order": order,
                "click_state2": "active",
                "username": username,
                "img_head": img_head
            })
        else:
            if request.GET.get("order") == "min_max":  # 从小到大
                hengyan = HengYanModel.objects.order_by('click')  # 升序
                state1 = "success"
                state2 = "text"
                order = "min_max"
            else:
                hengyan = HengYanModel.objects.order_by('-click')  # 降序
                state1 = "text"
                state2 = "success"
                order = "max_min"
            three_sort = []
            for zh in hengyan:
                if zh.type == "都市":
                    three_sort.append(zh)
            for zh in three_sort:
                for i in range(0, len(zh.info), 30):
                    zh.info = zh.info[:i] + "<p>" + zh.info[i:] + "</p>"
            data = get_pager(three_sort, request)[0]
            return render(request, 'hengyan.html', context={
                'data': data, "hengyan": get_pager(three_sort, request)[1],
                "three_state": "success",
                'sort': "three_sort",
                "state1": state1,
                "state2": state2,
                "order": order,
                "click_state2": "active",
                "username": username,
                "img_head": img_head
            })


class ChuangShiView(View):
    def get(self, request):
        ret = request.get_signed_cookie("is_login", default="0", salt="already_login")
        username = LoginStateModel.objects.all()[0].login_state
        login_user = LoginModel.objects.filter(username=username)[0]
        img_head = login_user.img_head
        if ret == "1":  # 如果为1，代表已经登陆成功
            if request.GET.get("state") == "false":
                logout(request)
                # 退出登录，重定向到登录页
                response = redirect("/login/")
                # 退出登录时清除cookie中的is_login
                response.delete_cookie('is_login')
                return redirect("/login/")
            else:
                chuangshi = ChuangShiModel.objects.all()
                for cs in chuangshi:
                    for i in range(0, len(cs.info), 30):
                        cs.info = cs.info[:i] + "<p>" + cs.info[i:] + "</p>"
                data = get_pager(chuangshi, request)[0]
                return render(request, 'chuangshi.html', context={
                    'data': data, "chuangshi": get_pager(chuangshi, request)[1],
                    "click_state3": "active", "username": username, "img_head": img_head
                })
        else:
            return redirect("/login/")


class ChuangShiSortView(View):

    def get(self, request):
        username = LoginStateModel.objects.all()[0].login_state
        login_user = LoginModel.objects.filter(username=username)[0]
        img_head = login_user.img_head
        if request.GET.get("sort") == "one_sort":
            if request.GET.get("order") == "min_max":  # 从小到大
                chuangshi = ChuangShiModel.objects.order_by('collection')  # 升序
                state1 = "success"
                state2 = "text"
                order = "min_max"
            else:
                chuangshi = ChuangShiModel.objects.order_by('-collection')  # 降序
                state1 = "text"
                state2 = "success"
                order = "max_min"
            one_sort = []
            for zh in chuangshi:
                if zh.type == "[玄幻]":
                    one_sort.append(zh)
            for zh in one_sort:
                for i in range(0, len(zh.info), 30):
                    zh.info = zh.info[:i] + "<p>" + zh.info[i:] + "</p>"
                for i in range(0, len(zh.label), 12):
                    zh.label = zh.label[:i] + "<p>" + zh.label[i:] + "</p>"
            data = get_pager(one_sort, request)[0]
            return render(request, 'chuangshi.html', context={
                'data': data, "chuangshi": get_pager(one_sort, request)[1],
                "one_state": "success",
                'sort': "one_sort",
                "state1": state1,
                "state2": state2,
                "order": order,
                "click_state3": "active",
                "username": username,
                "img_head": img_head
            })
        elif request.GET.get("sort") == "two_sort":
            if request.GET.get("order") == "min_max":  # 从小到大
                chuangshi = ChuangShiModel.objects.order_by('collection')  # 升序
                state1 = "success"
                state2 = "text"
                order = "min_max"
            else:
                chuangshi = ChuangShiModel.objects.order_by('-collection')  # 降序
                state1 = "text"
                state2 = "success"
                order = "max_min"
            two_sort = []
            for zh in chuangshi:
                if zh.type == "[武侠]":
                    two_sort.append(zh)
            for zh in two_sort:
                for i in range(0, len(zh.info), 30):
                    zh.info = zh.info[:i] + "<p>" + zh.info[i:] + "</p>"
                for i in range(0, len(zh.label), 12):
                    zh.label = zh.label[:i] + "<p>" + zh.label[i:] + "</p>"
            data = get_pager(two_sort, request)[0]
            return render(request, 'chuangshi.html', context={
                'data': data, "chuangshi": get_pager(two_sort, request)[1],
                "two_state": "success",
                'sort': "two_sort",
                "state1": state1,
                "state2": state2,
                "order": order,
                "click_state3": "active",
                "username": username,
                "img_head": img_head
            })
        elif request.GET.get("sort") == "all_sort":
            if request.GET.get("order") == "min_max":  # 从小到大
                chuangshi = ChuangShiModel.objects.order_by('collection')  # 升序
                state1 = "success"
                state2 = "text"
                order = "min_max"
            else:
                chuangshi = ChuangShiModel.objects.order_by('-collection')  # 降序
                state1 = "text"
                state2 = "success"
                order = "max_min"
            for zh in chuangshi:
                for i in range(0, len(zh.info), 30):
                    zh.info = zh.info[:i] + "<p>" + zh.info[i:] + "</p>"
                for i in range(0, len(zh.label), 12):
                    zh.label = zh.label[:i] + "<p>" + zh.label[i:] + "</p>"
            data = get_pager(chuangshi, request)[0]
            return render(request, 'chuangshi.html', context={
                'data': data, "chuangshi": get_pager(chuangshi, request)[1],
                "all_state": "success",
                'sort': "all_sort",
                "state1": state1,
                "state2": state2,
                "order": order,
                "click_state3": "active",
                "username": username,
                "img_head": img_head
            })
        else:
            if request.GET.get("order") == "min_max":  # 从小到大
                chuangshi = ChuangShiModel.objects.order_by('collection')  # 升序
                state1 = "success"
                state2 = "text"
                order = "min_max"
            else:
                chuangshi = ChuangShiModel.objects.order_by('-collection')  # 降序
                state1 = "text"
                state2 = "success"
                order = "max_min"
            three_sort = []
            for zh in chuangshi:
                if zh.type == "[都市]":
                    three_sort.append(zh)
            for zh in three_sort:
                for i in range(0, len(zh.info), 30):
                    zh.info = zh.info[:i] + "<p>" + zh.info[i:] + "</p>"
                for i in range(0, len(zh.label), 12):
                    zh.label = zh.label[:i] + "<p>" + zh.label[i:] + "</p>"
            data = get_pager(three_sort, request)[0]
            return render(request, 'chuangshi.html', context={
                'data': data, "chuangshi": get_pager(three_sort, request)[1],
                "three_state": "success",
                'sort': "three_sort",
                "state1": state1,
                "state2": state2,
                "order": order,
                "click_state3": "active",
                "username": username,
                "img_head": img_head
            })
