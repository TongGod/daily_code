import csv

import requests
from fake_useragent import UserAgent
import time


class LaGou:
    def __init__(self, cookie):
        self.post_url = "https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false"
        self.cookie = cookie
        self.headers = {
            "user-agent": UserAgent().random,
            "origin": "https://www.lagou.com",
            "referer": "https://www.lagou.com/jobs/list_%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90/p-city_0?&cl=false&fromSearch=true&labelWords=&suginput=",
            "accept": "application/json, text/javascript, */*; q=0.01",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "zh-CN,zh;q=0.9",
            "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
            "x-requested-with": "XMLHttpRequest",
            "cookie": self.cookie
        }
        self.count = 0

    def get_post_json(self, pn):
        data = {
            "first": "false",
            "pn": pn,
            "kd": "大数据",
        }
        if pn == 1:
            data["first"] = "True"
        r = requests.post(self.post_url, headers=self.headers, data=data)
        print(r.text)
        return r.json()

    def process_data(self, data_dict):
        recruit_list = []
        result_list = data_dict["content"]["positionResult"]["result"]
        for result in result_list:
            recruit = {"地区": result["city"] + " " + result["district"], "学历": result["education"],
                       "薪酬": result["salary"], "经验": result["workYear"], "岗位": result["positionName"],
                       "公司规模": result["companySize"], "发布日期": result["createTime"], "行业类别": result["firstType"]}
            recruit_list.append(recruit)

        return recruit_list

    # 保存到csv
    def csv_writer(self, recruit_list):
        for recruit in recruit_list:
            self.count = self.count + 1
            title = list(recruit.keys())
            with open('data.csv', 'a', newline='', encoding='utf-8') as f:
                writer = csv.DictWriter(f, fieldnames=title)  # 提前预览列名，当下面代码写入数据时，会将其一一对应。
                if self.count == 1:
                    writer.writeheader()  # 写入列名
                writer.writerow(recruit)


if __name__ == '__main__':

    cookie = input("请输入浏览器中的cookie信息：")
    lagou = LaGou(cookie)
    out = 0
    for i in range(1, 70):
        out = out + 1
        while True:
            try:
                data_json = lagou.get_post_json(i)
                recruit_list = lagou.process_data(data_json)
                lagou.csv_writer(recruit_list)
                break
            except KeyError:
                lagou.cookie = input("被识别出爬虫，请刷新浏览器输入浏览器的cookie信息：")
                continue
            break
        time.sleep(4)
        print("第%d页数据已经写入成功！！！" % out)
