import json
import random
import threading
import time

import requests
from fake_useragent import UserAgent
import csv
import re


class Spider_51job:
    # 初始化，设置好请求头
    def __init__(self):

        self.headers = {
            "User-Agent": UserAgent().random,
            "Host": "search.51job.com",
        }
        self.num = 0
        self.counts = 0

    # 获取请求网页的源码
    def get_html_text(self, url):
        r = requests.get(url, headers=self.headers)
        return r.text

    # 解析网页，获得想要的数据
    def analysis_html(self, text_html):
        # 使用正则匹配网页中的json字符串
        result_str = re.findall('"market_ads\":\[\],(.*?),\"jobid_count\"', text_html, re.S)[0]
        # 将json字符串转换为字典
        data_dict = json.loads("{" + result_str + "}")
        return data_dict

    # 进行数据处理，获得需要的信息
    def get_info(self, data_dict):
        title, provide_salary, company_type, company_ind, company_size = [], [], [], [], []
        attribute = []
        data_list = data_dict["engine_search_result"]  # 取出一页的岗位数据列表
        for data in data_list:
            title.append(data["job_name"])  # 岗位名称
            provide_salary.append(data["providesalary_text"])  # 薪资
            company_type.append(data["companytype_text"])  # 公司单位所属
            company_size.append(data["companysize_text"])  # 公司规模
            company_ind.append(data["companyind_text"])  # 公司类型
            attribute.append(data["attribute_text"])  # 岗位地点、经验、学历、所招人数
        job_info = [title, provide_salary, company_type, company_size, company_ind, attribute]
        return job_info

    # 将数据保存到csv
    def csv_info(self, job_info):
        # 将数据写入文件
        with open("./unprocess_data2.csv", "a", newline="") as cf:
            w = csv.writer(cf)
            for i in range(0, len(job_info[0])):
                # 将数据写入csv
                w.writerow(
                    [job_info[0][i], job_info[1][i], job_info[2][i], job_info[3][i], job_info[4][i], job_info[5][i]])
if __name__ == '__main__':
    # 要爬取的关键字
    key = '大数据'
    job = Spider_51job()
    # 生成前200页的url
    urls = [
        'https://search.51job.com/list/000000,000000,0000,00,9,99,' + key + ',2,{}.html?lang=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='.format(
            i) for i in range(1, 201)]
    # 首次写的时候，打开文件写入表头
    f = open('./unprocess_data2.csv', 'a', encoding='utf-8', newline='')
    csv_writer = csv.writer(f)
    csv_writer.writerow(["title", "provide_salary", "company_type", "company_size", "company_ind", "attribute"])
    f.close()
    # 循环开始爬取网页

    for url in urls:
        job.num = job.num + 1
        text_html = job.get_html_text(url)
        data_dict = job.analysis_html(text_html)
        job_info = job.get_info(data_dict)
        print("第%d页数据爬取成功！！" % job.num)
        job.csv_info(job_info)
        print("第%d页数据存储成功！！" % job.num)
        print("=" * 30)
        # 设置延时，从1秒到3秒随机一个时间延时，防止请求太快被检测出来
