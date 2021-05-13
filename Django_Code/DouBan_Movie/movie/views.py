import json

from PIL import Image
from django.contrib.auth import logout
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from django.core.paginator import Paginator
from django.shortcuts import render, HttpResponse, redirect

import numpy as np
from django.urls import reverse

from .models import MovieModel, LoginStateModel
from login.models import LoginModel
from django.views.generic import View


# 首页
class HomePageView(View):
    def get(self, request):
        ret = request.get_signed_cookie("is_login", default="0", salt="already_login")
        if ret == "1":  # 如果为1，代表已经登陆成功
            if request.GET.get("state") == "false":
                logout(request)
                # 退出登录，重定向到登录页
                response = redirect("/login/")
                # 退出登录时清除cookie中的is_login
                response.delete_cookie('is_login')
                return response
            else:
                user = LoginStateModel.objects.all()[0].user_state
                rep = redirect(reverse("home", kwargs={"username": user}))
                return rep
        else:  # 如果不为"1"，即返回到登陆页面
            return redirect("/login/")


# 全部影视数据
class HomeView(View):
    def get(self, request, username):
        # 获取当前浏览器"is_login"的cookie值
        ret = request.get_signed_cookie("is_login", default="0", salt="already_login")
        if ret == "1":  # 如果为1，代表已经登陆成功
            if len(LoginStateModel.objects.all()) != 0:
                LoginStateModel.drop_collection()  # 删除集合
                LoginStateModel(user_state=username).save()
            else:
                LoginStateModel(user_state=username).save()
            if request.GET.get("state") == "false":
                logout(request)
                # 退出登录，重定向到登录页
                response = redirect("/login/")
                # 退出登录时清除cookie中的is_login
                response.delete_cookie('is_login')
                return response
            else:
                movie = MovieModel.objects.all()  # 导入的MovieModel模型
                p = Paginator(movie, 10)  # 分页，10个电影信息一页
                if p.num_pages <= 1:  # 如果文章不足一页
                    movie_list = movie  # 直接返回所有文章
                    data = ''  # 不需要分页按钮
                else:
                    page = int(request.GET.get('page', 1))  # 获取请求的文章页码，默认为第一页
                    movie_list = p.page(page)  # 返回指定页码的页面
                    left = []  # 当前页左边连续的页码号，初始值为空
                    right = []  # 当前页右边连续的页码号，初始值为空
                    left_has_more = False  # 标示第 1 页页码后是否需要显示省略号
                    right_has_more = False  # 标示最后一页页码前是否需要显示省略号
                    first = False  # 标示是否需要显示第 1 页的页码号。
                    # 因为如果当前页左边的连续页码号中已经含有第 1 页的页码号，此时就无需再显示第 1 页的页码号，
                    # 其它情况下第一页的页码是始终需要显示的。
                    # 初始值为 False
                    last = False  # 标示是否需要显示最后一页的页码号。
                    total_pages = p.num_pages
                    page_range = p.page_range
                    if page == 1:  # 如果请求第1页
                        right = page_range[page:page + 2]  # 获取右边连续号码页
                        if right[-1] < total_pages - 1:  # 如果最右边的页码号比最后一页的页码号减去 1 还要小，
                            # 说明最右边的页码号和最后一页的页码号之间还有其它页码，因此需要显示省略号，通过 right_has_more 来指示。
                            right_has_more = True
                        if right[-1] < total_pages:  # 如果最右边的页码号比最后一页的页码号小，说明当前页右边的连续页码号中不包含最后一页的页码
                            # 所以需要显示最后一页的页码号，通过 last 来指示
                            last = True
                    elif page == total_pages:  # 如果请求最后一页
                        left = page_range[(page - 3) if (page - 3) > 0 else 0:page - 1]  # 获取左边连续号码页
                        if left[0] > 2:
                            left_has_more = True  # 如果最左边的号码比2还要大，说明其与第一页之间还有其他页码，因此需要显示省略号，通过 left_has_more 来指示
                        if left[0] > 1:  # 如果最左边的页码比1要大，则要显示第一页，否则第一页已经被包含在其中
                            first = True
                    else:  # 如果请求的页码既不是第一页也不是最后一页
                        left = page_range[(page - 3) if (page - 3) > 0 else 0:page - 1]  # 获取左边连续号码页
                        right = page_range[page:page + 2]  # 获取右边连续号码页
                        if left[0] > 2:
                            left_has_more = True
                        if left[0] > 1:
                            first = True
                        if right[-1] < total_pages - 1:
                            right_has_more = True
                        if right[-1] < total_pages:
                            last = True
                    data = {  # 将数据包含在data字典中
                        'left': left,
                        'right': right,
                        'left_has_more': left_has_more,
                        'right_has_more': right_has_more,
                        'first': first,
                        'last': last,
                        'total_pages': total_pages,
                        'page': page
                    }
                # 判断是否已经点赞
                # 查询该用户锁点赞的电影
                already_movie_id = []
                name = LoginStateModel.objects.all()[0].user_state  # 获取到当前登录的用户名
                already_save = LoginModel.objects.filter(user_name=name)[0].clike_info
                for index in range(0, len(already_save)):
                    already_movie_id.append(already_save[index].id)
                for move in movie_list:
                    if move.id in already_movie_id:
                        move.click_state = "glyphicon glyphicon-heart"
                login_user = LoginModel.objects.filter(user_name=name)[0]
                img = login_user.img_head
                return render(request, 'home.html', context={
                    'movie_list': movie_list, 'data': data, "username": username, "img_head": img
                })
        else:  # 如果不为"1"，即返回到登陆页面
            return redirect("/login/")


# 搜索模块
class SearchView(View):
    def get(self, request, username):
        # 获取当前浏览器"is_login"的cookie值
        ret = request.get_signed_cookie("is_login", default="0", salt="already_login")
        if ret == "1":  # 如果为1，代表已经登陆成功
            # 年份区间
            min_year = request.GET.get("min_year")
            max_year = request.GET.get("max_year")

            # 电影类型
            movie_type = request.GET.get("movie_type")
            # 制片国家
            movie_country = request.GET.get("movie_country")

            # 查询出所有的数据
            movie = MovieModel.objects.all()  # 导入的MovieModel模型
            # 判断是否已经点赞
            # 查询该用户锁点赞的电影
            already_movie_id = []
            already_save = LoginModel.objects.filter(user_name=username)[0].clike_info
            for index in range(0, len(already_save)):
                already_movie_id.append(already_save[index].id)
            for m in movie:
                if m.id in already_movie_id:
                    m.click_state = "glyphicon glyphicon-heart"
            year_movie = []
            # 年份区间的查找处理
            for m in movie:
                if min_year is not None and str(
                        max_year) is not None and min_year != "" and max_year != "":  # # 最大最小年份都不为空
                    if m.year in [str(i) for i in range(int(min_year), int(max_year))]:
                        year_movie.append(m)
                elif min_year == "" and max_year == "":  # 最大最小年份都为空
                    year_movie.append(m)
                elif min_year == "" and max_year != "":  # 最小年份为空
                    if m.year in [str(i) for i in range(1900, int(max_year))]:
                        year_movie.append(m)
                else:  # min_year != "" and max_year == "":  # 最大年份为空
                    if m.year in [str(i) for i in range(int(min_year), 2022)]:
                        year_movie.append(m)
            # 评分区间
            min_rate = request.GET.get("min_rate")
            max_rate = request.GET.get("max_rate")
            rating_movie = []
            for y in year_movie:
                if min_rate is not None and str(
                        max_rate) is not None and min_rate != "" and max_rate != "":  # # 最大最小年份都不为空
                    # 处理最大的评论区间
                    # 1.如果输入最大区间和最小区间的是整数
                    if eval(min_rate) <= eval(y.score) <= eval(max_rate):
                        rating_movie.append(y)
                else:
                    rating_movie.append(y)
            # 电影类型
            type_movie_list = []
            for t in rating_movie:
                if movie_type in t.type:
                    type_movie_list.append(t)
            country_movie_list = []
            for c in type_movie_list:
                if movie_country in c.country:
                    country_movie_list.append(c)
            movie = country_movie_list
            p = Paginator(movie, 10)  # 分页，10个电影信息一页
            if p.num_pages <= 1:  # 如果文章不足一页
                movie_list = movie  # 直接返回所有文章
                data = ''  # 不需要分页按钮
            else:
                page = int(request.GET.get('page', 1))  # 获取请求的文章页码，默认为第一页
                movie_list = p.page(page)  # 返回指定页码的页面
                left = []  # 当前页左边连续的页码号，初始值为空
                right = []  # 当前页右边连续的页码号，初始值为空
                left_has_more = False  # 标示第 1 页页码后是否需要显示省略号
                right_has_more = False  # 标示最后一页页码前是否需要显示省略号
                first = False  # 标示是否需要显示第 1 页的页码号。
                # 因为如果当前页左边的连续页码号中已经含有第 1 页的页码号，此时就无需再显示第 1 页的页码号，
                # 其它情况下第一页的页码是始终需要显示的。
                # 初始值为 False
                last = False  # 标示是否需要显示最后一页的页码号。
                total_pages = p.num_pages
                page_range = p.page_range
                if page == 1:  # 如果请求第1页
                    right = page_range[page:page + 2]  # 获取右边连续号码页
                    if right[-1] < total_pages - 1:  # 如果最右边的页码号比最后一页的页码号减去 1 还要小，
                        # 说明最右边的页码号和最后一页的页码号之间还有其它页码，因此需要显示省略号，通过 right_has_more 来指示。
                        right_has_more = True
                    if right[-1] < total_pages:  # 如果最右边的页码号比最后一页的页码号小，说明当前页右边的连续页码号中不包含最后一页的页码
                        # 所以需要显示最后一页的页码号，通过 last 来指示
                        last = True
                elif page == total_pages:  # 如果请求最后一页
                    left = page_range[(page - 3) if (page - 3) > 0 else 0:page - 1]  # 获取左边连续号码页
                    if left[0] > 2:
                        left_has_more = True  # 如果最左边的号码比2还要大，说明其与第一页之间还有其他页码，因此需要显示省略号，通过 left_has_more 来指示
                    if left[0] > 1:  # 如果最左边的页码比1要大，则要显示第一页，否则第一页已经被包含在其中
                        first = True
                else:  # 如果请求的页码既不是第一页也不是最后一页
                    left = page_range[(page - 3) if (page - 3) > 0 else 0:page - 1]  # 获取左边连续号码页
                    right = page_range[page:page + 2]  # 获取右边连续号码页
                    if left[0] > 2:
                        left_has_more = True
                    if left[0] > 1:
                        first = True
                    if right[-1] < total_pages - 1:
                        right_has_more = True
                    if right[-1] < total_pages:
                        last = True
                data = {  # 将数据包含在data字典中
                    'left': left,
                    'right': right,
                    'left_has_more': left_has_more,
                    'right_has_more': right_has_more,
                    'first': first,
                    'last': last,
                    'total_pages': total_pages,
                    'page': page
                }
            page_data = {
                'min_year': min_year,
                'max_year': max_year,
                'min_rate': min_rate,
                'max_rate': max_rate,
                'movie_type': movie_type,
                'movie_country': movie_country
            }
            return render(request, 'search.html', context={
                'movie_list': movie_list, 'data': data, 'page_data': page_data, "username": username
            })
        else:  # 如果不为"1"，即返回到登陆页面
            return redirect("/login/")


# 统计信息
class StaInfoView(View):
    def get(self, request):
        movie = MovieModel.objects.all()
        username = LoginStateModel.objects.all()[0].user_state
        id = request.GET.get("id")
        if id == 'year':
            movie_year = []
            for m in movie:
                movie_year.append(m.year)
            year_count = dict(zip(*np.unique(movie_year, return_counts=True)))
            year_name = list(year_count.keys())
            year_num = list(year_count.values())
            year_data = []
            start = 1931
            for i in range(0, 9):
                count = 0
                end = start + 10
                section = [k for k in range(start, end)]
                for y in range(0, len(year_name)):
                    if eval(year_name[y]) in section:
                        count = count + year_num[y]
                year_data.append({
                    "name": "[" + str(start) + "," + str(end) + ")",
                    "value": count,
                    "username": username
                })
                start = start + 10
            return render(request, 'year_draw.html', {"year_data": year_data})
        if id == 'type':
            type_str = ""
            for m in movie:
                type_str = type_str + m.type + " "
            type_sp_list = type_str.split(" ")
            type_count = dict(zip(*np.unique(type_sp_list, return_counts=True)))
            type_name = list(type_count.keys())
            type_num = list(type_count.values())
            type_data = []
            for t in range(0, len(type_name)):
                type_data.append({
                    "name": type_name[t],
                    "value": type_num[t],
                    "username": username
                })
            s_data = type_name[:int(len(type_name) / 2)]
            e_data = type_name[int(len(type_name) / 2):]
            return render(request, 'type_draw.html', {"type_data": type_data, "s_data": s_data, "e_data": e_data})
        if id == 'rate':
            sum_list = []
            for i in range(8, 10):
                for j in range(0, 10):
                    sum_list.append(i + eval("0." + str(j)))
            section = [sum_list[:5], sum_list[5:10], sum_list[10:15], sum_list[15:20]]
            rate_num = []
            for s in section:
                count = 0
                for m in movie:
                    if eval(m.score) in s:
                        count = count + 1
                rate_num.append(count)
            rate_date = []
            for d in range(0, len(section)):
                rate_date.append(
                    {"name": "[" + str(section[d][0]) + "-" + str(section[d][-1]) + "]", "value": rate_num[d]})
            return render(request, 'rate_draw.html', {"rate_date": rate_date, "username": username})
        if id == 'country':
            country_str = ''
            for m in movie:
                country_str = country_str + m.country + " "
            country_sp_list = country_str.split(" ")
            country_count = dict(zip(*np.unique(country_sp_list, return_counts=True)))
            del country_count['']
            country_name = list(country_count.keys())
            country_num = list(country_count.values())
            return render(request, 'country_draw.html',
                          {"country_name": country_name, "country_num": country_num, "username": username})
        if id == 'rank':
            rank_top = []
            rank_score = []
            for m in movie:
                rank_top.append(int(m.top))
                rank_score.append(round(float(m.score), 1))
            data = []
            for r in range(0, len(rank_top)):
                data.append([rank_score[r], rank_top[r]])
            return render(request, 'rank_draw.html', {"data": data, "username": username})


# 个人中心
class UserInfoView(View):
    def get(self, request):
        username = LoginStateModel.objects.all()[0].user_state  # 获取到当前登录的用户名
        password = LoginModel.objects.filter(user_name=username)[0].password  # 获取当前登录的密码
        # 获取该用户的已经评论过的电影信息以及评论信息
        info = []
        movie = MovieModel.objects.all()
        for i in range(0, len(movie)):
            for j in movie[i].comment_info:
                if j[0] == username:
                    info.append([j[1], movie[i].name_chinese])
        login_user = LoginModel.objects.filter(user_name=username)[0]
        img_head = login_user.img_head
        data = {
            "username": username,
            "password": password,
            "com_list": info,
            "img_head": img_head
        }

        return render(request, 'user_info.html', context=data)


# 个人中心修改资料以及删除评论
class ModifyUserView(View):
    def post(self, request):
        name = request.POST.get("name")  # 获取到要修改的用户名
        pwd = request.POST.get("pwd")  # 获取到要修改的密码
        username = LoginStateModel.objects.all()[0].user_state  # 获取到当前登录的用户名
        if len(name) != 0 and len(pwd) != 0:
            movie = MovieModel.objects.all()
            com_list = []
            already_data_list = []
            for i in range(0, len(movie)):
                for j in movie[i].comment_info:
                    if j[0] == username:
                        com_list.append([name, j[1]])
                        already_data_list.append([j[0], j[1]])
                    else:
                        com_list.append([j[0], j[1]])
                        already_data_list.append([j[0], j[1]])
            handler = MovieModel.objects.filter(comment_info=already_data_list)
            handler.comment_info = already_data_list

            img = request.FILES.get("face")
            if img is not None:
                path = default_storage.save("static/images/" + username + ".png", ContentFile(img.read()))
                login_user = LoginModel.objects.get(user_name=username)
                login_user.img_head = path
                login_user.save()

            # 修改登录状态的用户名
            login_state = LoginStateModel.objects.get(user_state=username)
            login_state.user_state = name
            login_state.save()
            # 修改用户名 和 密码
            modify_name = LoginModel.objects.get(user_name=username)
            modify_name.user_name = name
            modify_name.password = pwd
            modify_name.save()
            # 修改 该用户名评论的电影的用户名数据

            return redirect('user')
        if len(name) == 0 and len(pwd) != 0:
            modify_name = LoginModel.objects.get(user_name=username)
            modify_name.password = pwd
            modify_name.save()

            img = request.FILES.get("face")
            if img is not None:
                path = default_storage.save("static/images/" + username + ".png", ContentFile(img.read()))
                login_user = LoginModel.objects.get(user_name=username)
                login_user.img_head = path
                login_user.save()
            return redirect('user')
        if len(name) != 0 and len(pwd) == 0:
            movie = MovieModel.objects.all()
            com_list = []
            already_data_list = []
            for i in range(0, len(movie)):
                for j in movie[i].comment_info:
                    if j[0] == username:
                        com_list.append([name, j[1]])
                        already_data_list.append([j[0], j[1]])
                    else:
                        com_list.append([j[0], j[1]])
                        already_data_list.append([j[0], j[1]])
            handler = MovieModel.objects.filter(comment_info=already_data_list)
            handler.comment_info = already_data_list

            img = request.FILES.get("face")
            if img is not None:
                path = default_storage.save("static/images/" + username + ".png", ContentFile(img.read()))

                login_user = LoginModel.objects.get(user_name=username)
                login_user.img_head = path
                login_user.save()

            # 修改登录状态的用户名
            login_state = LoginStateModel.objects.get(user_state=username)
            login_state.user_state = name
            login_state.save()

            modify_name = LoginModel.objects.get(user_name=username)
            modify_name.user_name = name
            modify_name.save()

            return redirect('user')
        if len(name) == 0 and len(pwd) == 0:
            img = request.FILES.get("face")
            if img is not None:
                path = default_storage.save("static/images/" + username + ".png", ContentFile(img.read()))
                login_user = LoginModel.objects.get(user_name=username)
                login_user.img_head = path
                login_user.save()
            return redirect('user')


# 点赞
class ClickCommentView(View):
    def get(self, request):
        username = request.GET.get("username")
        name = request.GET.get("name")
        movie = MovieModel.objects.filter(name_chinese=name)[0]
        if request.GET.get("heart") == "add":
            # 该用户已经点击的数量
            already_save = LoginModel.objects.filter(user_name=username)[0].clike_info
            global flag
            flag = True
            if len(already_save) != 0:
                for i in range(0, len(already_save)):
                    # 如果点击的已经在数据中存在，则进行取消点赞
                    if movie.id == already_save[i].id:
                        flag = False
                        likes_count = MovieModel.objects.filter(name_chinese=name)[0].likes_num
                        MovieModel.objects.filter(name_chinese=name).update(likes_num=likes_count - 1)
                        data_dic = {"class_name": "glyphicon glyphicon-heart-empty"}
                        return HttpResponse(json.dumps(data_dic))
                if flag:
                    MovieModel.objects.filter(name_chinese=name).update(likes_num=movie.likes_num + 1)
                    LoginModel.objects(user_name=username).update_one(push__clike_info=movie)
                    data_dic = {"class_name": "glyphicon glyphicon-heart"}
                    return HttpResponse(json.dumps(data_dic))
            else:
                MovieModel.objects.filter(name_chinese=name).update(likes_num=movie.likes_num + 1)
                LoginModel.objects(user_name=username).update_one(push__clike_info=movie)
                data_dic = {"class_name": "glyphicon glyphicon-heart"}
                return HttpResponse(json.dumps(data_dic))
        if request.GET.get("heart") == "reduce":
            likes_count = MovieModel.objects.filter(name_chinese=name)[0].likes_num
            MovieModel.objects.filter(name_chinese=name).update(likes_num=likes_count - 1)
            LoginModel.objects.filter(user_name=username).update_one(pull__clike_info=movie)
            data_dic = {"class_name": "glyphicon glyphicon-heart-empty"}
            return HttpResponse(json.dumps(data_dic))
        return HttpResponse("404")


# 评论
class CommentInfoView(View):
    def post(self, request):
        user_name = request.POST.get("user_name")
        com_info = request.POST.get("com_info")  # 获取文本域的信息
        if len(com_info) == 0:  # 如果提交的为空值，则进行相应的提示
            print("为空！")
        else:
            # 获取到评论进行保存
            movie_name = request.POST.get("movie_name")
            login_model = LoginModel.objects.get(user_name=user_name)
            img_head = login_model.img_head
            MovieModel.objects(name_chinese=movie_name).update_one(push__comment_info=[user_name, com_info, img_head])

        return redirect(reverse("home", kwargs={"username": user_name}))
