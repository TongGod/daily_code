# @Time    : 2021/4/14 14:14
# @Author  : GodWei
# @File    : hengyan_spider.py
import csv
import time

import requests
from lxml import etree
from fake_useragent import UserAgent


class HengYanSpider:
    def __init__(self):
        # 请求头
        self.headers = {
            "User-Agent": UserAgent().random,
            "Host": "top.hengyan.com",
            "Referer": "http://top.hengyan.com/xuanhuan/",
        }
        # 恒言中文网
        self.xuanhuan = "http://top.hengyan.com/xuanhuan/default.aspx?p={}"
        self.dushi = "http://top.hengyan.com/dushi/default.aspx?p={}"
        self.mm = "http://top.hengyan.com/mm/default.aspx?p={}"

        self.count = 0

    def url_text(self, url):
        r = requests.get(url=url)
        return r.text

    def url_join(self):
        url_list = []
        for j in range(1, 3):
            url_list.append(self.xuanhuan.format(j))
        for j in range(1, 3):
            url_list.append(self.mm.format(j))
        for j in range(1, 4):
            url_list.append(self.dushi.format(j))
        return url_list

    # 获取每本小说的详情链接
    def url_deep(self, url):
        text = self.url_text(url)
        html = etree.HTML(text)
        detail_url_list = html.xpath("//div[@class='list']//ul[not(contains(@class,'title'))]//li["
                                     "@class='bookname']/a[1]/@href")
        return detail_url_list

    def save_csv(self, top, bookname, click, info_str, label, type):
        with open("./hengyan_data.csv", "a", newline="", encoding='utf-8') as cf:
            w = csv.writer(cf)
            w.writerow([top, bookname, click, info_str, label, type])

    def url_analysis(self, url):
        detail_url_list = self.url_deep(url)
        for i in detail_url_list:
            self.count = self.count + 1
            text = self.url_text(i)
            html = etree.HTML(text)
            bookname = html.xpath("//div[@class='des']/h2//text()")
            if len(bookname) != 0:
                bookname = html.xpath("//div[@class='des']/h2//text()")[0]
                click = html.xpath("//p[@class='info']/span[1]//text()")[0][:-2]
                info = html.xpath("//p[contains(@class,'intro')]//text()")
                info_str = ""
                for n in info:
                    info_str = info_str + str(n).strip() + "\n"
                if len(html.xpath("//p[@class='biaoqian']//label//text()")) == 0:
                    label = "暂无"
                else:
                    label = html.xpath("//p[@class='biaoqian']//label//text()")[0]
                type = html.xpath("//p[@class='info']/span[2]/a//text()")[0]
                # 保存数据
                self.save_csv(self.count, bookname, click, info_str, label, type)
                print(bookname, "爬取并保存成功")


def hengyan_main():
    hengyan = HengYanSpider()
    hengyan_list = hengyan.url_join()  # 组建url
    # 首次写的时候，打开文件写入表头
    f = open('./hengyan_data.csv', 'a', encoding='utf-8', newline='')
    csv_writer = csv.writer(f)
    csv_writer.writerow(["top", "bookname", "click", "info", "label", "type"])
    f.close()
    url_list = [hengyan_list[:2], hengyan_list[2:4], hengyan_list[4:]]
    for j in url_list:
        hengyan.count = 0
        for i in j:
            hengyan.url_analysis(i)
            print("{}爬取并保存成功".format(i))
            time.sleep(0.5)
    print("*-*-*-*-*-*-恒言小说网数据爬取并保存完毕-*-*-*-*-*-*")
