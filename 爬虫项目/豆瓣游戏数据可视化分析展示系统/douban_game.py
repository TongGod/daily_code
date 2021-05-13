import csv
import random
import requests
from fake_useragent import UserAgent
import time


class DouBan:
    def __init__(self):
        self.headers = {
            "User-Agent": UserAgent(verify_ssl=False).random,
            "Host": "www.douban.com",
            "Referer": "https://www.douban.com/game/explore?genres=&platforms=&q=&sort=rating"
        }

    def get_data_list(self, url):
        r = requests.get(url, headers=self.headers)
        return r.json()["games"]

    def analyse_data(self, data_list):
        # 平台，类型，评分，名称，评论人数
        platforms, type, rating, title, n_ratings = [], [], [], [], []
        for i in range(0, len(data_list)):
            platforms.append(data_list[i]['platforms'])
            type.append(data_list[i]['genres'])
            rating.append(data_list[i]['rating'])
            title.append(data_list[i]['title'])
            n_ratings.append(data_list[i]['n_ratings'])
        game_list = [title, type, rating, platforms, n_ratings]  # 名称，类型，评分，类型，平台，评论人数
        return game_list

    # 将数据保存到csv
    def csv_info(self, game_list):
        # 将数据写入文件
        with open("./data.csv", "a", newline="", encoding='utf-8') as cf:
            w = csv.writer(cf)
            for i in range(0, len(game_list[0])):
                w.writerow([game_list[0][i], game_list[1][i], game_list[2][i], game_list[3][i], game_list[4][i]])


if __name__ == '__main__':
    douban = DouBan()
    douban_api = "https://www.douban.com/j/ilmen/game/search?genres=&platforms=&q=&sort=rating&more="
    f = open('./data.csv', 'a', encoding='utf-8', newline='')
    csv_writer = csv.writer(f)
    # 构建列表头
    csv_writer.writerow(["title", "type", "rating", "platforms", "n_ratings"])
    f.close()
    num = 0
    for i in range(1, 201):
        num = num + 1
        douban_list = douban.get_data_list(url=douban_api + str(i))
        game_list = douban.analyse_data(douban_list)
        print("第%d页数据爬取成功！！！" % num)
        douban.csv_info(game_list)
        print("第%d页数据存储成功！！！" % num)
        print("=" * 30)
        time.sleep(random.randrange(1, 3))
