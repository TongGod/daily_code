import jieba
from django.shortcuts import render, HttpResponse
from game.models import GameInfo
from django.views.generic import View
import numpy as np
import re


# Create your views here.

class HomeView(View):

    def get(self, request):
        return render(request, 'home.html')


class SearchView(View):

    def post(self, request):
        global recommend
        result = request.POST.get('word')  # 获取用户输入的值
        game_info = GameInfo.objects.filter(title__contains=result)  # 按条件模糊查找
        game_list = []
        for info in game_info:
            if float(info.rating) >= 9.0:
                recommend = "推荐"
            elif 5.0 < float(info.rating) < 9.0:
                recommend = '可玩'
            else:
                recommend = '不推荐'
            game_list.append(
                {"title": info.title, "type": info.type, "rating": info.rating, "platforms": info.platforms,
                 "n_ratings": info.n_ratings, "recommend": recommend})
        return render(request, 'search.html', {"game_list": game_list, "result": result})


# 类型的平均游戏人数比较，每个类型的平均评分，每个类型评分9.0以上的数量，
class TypeRatingView(View):
    def get(self, request):
        if 'type' in request.GET:
            type_temp = []
            num_list = []
            count_avg = []  # 平均游戏人数比较
            avg_rating = []  # 平均评分
            rating_list = []  # 评分9.0以上的数量
            game_info = GameInfo.objects.all()
            for game in game_info:
                type_data = game.type.split('/')
                if len(type_data) >= 2:
                    type_temp.append(type_data[1].strip())
                    num_list.append(game.n_ratings)
            nore_type_list = dict(zip(*np.unique(type_temp, return_counts=True)))
            type_keys = list(nore_type_list.keys())
            for i in range(0, len(type_keys)):
                rating_count = 0  # 记录每个类型9.0评分以上的总和
                count = 0  # 记录每个类型的评论人数总和
                avg_rating_temp = 0  # 记录每个类型的评分总和
                num = 0
                for game in game_info:
                    for j in game.type.split('/'):
                        if type_keys[i] == j.strip():
                            if float(game.rating) >= 9.0:
                                rating_count = rating_count + 1
                            num = num + 1
                            avg_rating_temp = avg_rating_temp + float(game.rating)
                            count = count + float(game.n_ratings)
                rating_list.append(rating_count)  # 评分大于9.0的数量
                count_avg.append(int(count / num))  # 平均评论人数
                avg_rating.append(round((avg_rating_temp / num), 1))
            # 9.0评分数据小于25的标记其他做累加
            del_index = []
            other_sum = 0
            for r in range(0, len(rating_list)):
                if rating_list[r] < 25:
                    other_sum = other_sum + rating_list[r]
                    del_index.append(r)
            type_keys_list = []
            rating_list_process = []
            for d in range(0, len(type_keys)):
                if d not in del_index:
                    type_keys_list.append(type_keys[d])
                    rating_list_process.append(rating_list[d])
            type_keys_list.append('其他')
            rating_list_process.append(other_sum)
            pie_list = []  # 饼图数据列表
            for index in range(0, len(type_keys_list)):
                pie_list.append({'value': rating_list_process[index], 'name': type_keys_list[index]})
            type_data = {
                "type_x": type_keys_list,
                "type_y": count_avg,
                "rating_y": avg_rating,
                "pie_data": pie_list
            }
            return render(request, 'typedraw.html', type_data)
        elif 'platforms' in request.GET:
            game_info = GameInfo.objects.all()
            plat_list = []  # 初始平台列表
            rating_list = []  # 所有的评分
            for p in game_info:
                plat_list.append(str(p.platforms))
                rating_list.append(float(p.rating))
            # 平台数量分析
            plat_str = "/".join(plat_list)  # 列表拼接字符串
            split_plat = [i.strip() for i in plat_str.split("/")]
            plat_count = dict(zip(*np.unique(split_plat, return_counts=True)))
            plat_name = list(plat_count.keys())
            plat_value = list(plat_count.values())
            plat_data = []
            plat_choose = ["PC", "PS", "Switch", "iPhone"]
            other = 0
            # 平台评分
            rate_plat_list = []
            for i in plat_choose:
                count = 0
                for j in range(0, len(plat_name)):
                    if i in plat_name[j]:
                        count = count + plat_value[j]
                        if count > 8:
                            rate_plat_list.append(plat_name[j])
                            plat_data.append({"name": plat_name[j], "value": count})
                    else:
                        other = other + plat_value[j]
            plat_data.append({"其他": other})
            # 平台平均评分分析
            avg_list = []

            for i in range(0, len(rate_plat_list)):
                avg_count = 0
                avg_num = 0
                for j in range(0, len(plat_list)):
                    if rate_plat_list[i] in plat_list[j]:
                        # 只要有这个平台，累加
                        avg_count = avg_count + rating_list[j]
                        avg_num = avg_num + 1
                avg_list.append(round(float(avg_count / avg_num), 2))
            avg_dic = {
                "rate_plat_list": rate_plat_list,
                "avg_list": avg_list
            }
            return render(request, 'platdraw.html', {"plat_data": plat_data, "avg_dic": avg_dic})
        else:
            game_info = GameInfo.objects.all()
            game_str = ""
            for i in game_info:
                game_str = game_str + i.title
            res = re.findall('[\u4e00-\u9fa5a-zA-Z]', game_str, re.S)
            res_str = "".join(res)
            jieba_list = jieba.lcut(res_str)
            res_list = []
            for i in range(0, len(jieba_list)):
                if 2 < len(jieba_list[i]) < 10:
                    res_list.append(jieba_list[i])
            title_count = dict(zip(*np.unique(res_list, return_counts=True)))
            wordcloud_list = []
            for i in range(0, len(list(title_count.values()))):
                wordcloud_list.append({"name": list(title_count.keys())[i], "value": list(title_count.values())[i]})
            return render(request, 'wordcloud.html', {"wordcloud_list": wordcloud_list})
