# @Time    : 2021/4/16 8:19
# @Author  : GodWei
# @File    : zongheng_spider.py
import csv
import time
import re
import requests
from lxml import etree
from fake_useragent import UserAgent


class ZongHengSpider:
    def __init__(self):
        self.headers = {
            "User-Agent": UserAgent().random,
            "Host": "www.zongheng.com",
            "Referer": "http://www.zongheng.com/"
        }
        # 奇幻·玄幻
        self.xuanhuan = "http://www.zongheng.com/rank/details.html?rt=5&d=1&r=&i=2&c=1&p={}"
        # 都市·娱乐
        self.doushi = "http://www.zongheng.com/rank/details.html?rt=5&i=2&c=9&d=1&r=&p={}"
        # 武侠·仙侠
        self.wujia = "http://www.zongheng.com/rank/details.html?rt=5&i=2&c=3&d=1&r=&p={}"
        self.sort_list_url = [self.xuanhuan, self.doushi, self.wujia]

    def compose_url(self):
        url_list = []
        for url in self.sort_list_url:
            m_sort_page = []
            for i in range(1, 6):  # 每个类别5页
                m_sort_page.append(url.format(i))
            url_list.append(m_sort_page)
        return url_list

    def url_text(self, url):
        r = requests.get(url, headers=self.headers)
        return r.text

    def get_detail_url(self, out_url, type):
        html_text = self.url_text(out_url)
        html = etree.HTML(html_text)
        # 书名
        bookname_list = html.xpath("//div[@class='rank_d_b_name']/a//text()")
        # 简介
        bookinfo_list = html.xpath("//div[@class='rank_d_b_info']//text()")
        # 点击数
        click_list = re.findall("<div class=\"rank_d_b_ticket\">(.*?)<span>点击数</span></div>", html_text, re.S)
        # 排名
        top_list = html.xpath("//div[contains(@class,'rank_d_b_num')]//text()")
        # 详情url
        detail_url_list = html.xpath("//div[@class='rank_d_b_name']/a/@href")

        # 类别
        type_z = [type for i in range(0, len(detail_url_list))]

        # 返回
        return top_list, bookname_list, click_list, bookinfo_list, type_z, detail_url_list

    def detail_analysis(self, detail_url):
        # 取出标签
        detail_text = self.url_text(detail_url)
        html = etree.HTML(detail_text)
        label_str = " ".join(html.xpath("//div[@class='book-label']//span//a//text()"))
        return label_str

    def save_csv(self, data):
        with open("./zongheng_data.csv", "a", newline="", encoding='utf-8') as cf:
            w = csv.writer(cf)
            w.writerows(data)


def zongheng_main():
    zongheng = ZongHengSpider()
    url_list = zongheng.compose_url()  # 每个类别的url
    type_list = ['奇幻·玄幻', '都市·娱乐', '武侠·仙侠']
    f = open('./zongheng_data.csv', 'a', encoding='utf-8', newline='')
    csv_writer = csv.writer(f)
    csv_writer.writerow(["top", "bookname", "click", "info", "label", "type"])
    f.close()
    for url_i in range(0, len(url_list)):  # 三个大类别
        count = 0
        for u in url_list[url_i]:  # 每个类别的5页
            zongheng_list = zongheng.get_detail_url(u, type_list[url_i])
            detail_url_list = zongheng_list[-1]
            label_list = []
            for d in detail_url_list:
                label_list.append(zongheng.detail_analysis(d))
            top_list, bookname_list, click_list, bookinfo_list, type_z = zongheng_list[0], zongheng_list[1], \
                                                                         zongheng_list[2], zongheng_list[3], \
                                                                         zongheng_list[4]
            # 保存数据
            save_data = []
            for t in range(0, len(top_list)):
                save_data.append(
                    [top_list[t], bookname_list[t], click_list[t], bookinfo_list[t], label_list[t], type_z[t]])
            zongheng.save_csv(save_data)
            count = count + 1
            print("类别[{}]第{}页爬取并保存成功".format(type_list[url_i], count))
            time.sleep(0.6)
    print("*-*-*-*-*-*-纵横小说网数据爬取并保存完毕-*-*-*-*-*-*")
