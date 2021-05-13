import requests
from fake_useragent import UserAgent
from lxml import etree
import pandas as pd


class ChuangShiSpider:

    def __init__(self):
        # 请求头
        self.headers = {
            "User-Agent": UserAgent().random,
            "Host": "chuangshi.qq.com"
        }
        # 创世中文网
        self.xuanhuan = "http://chuangshi.qq.com/bang/fav/xh-zong.html"
        self.wuxia = "http://chuangshi.qq.com/bang/fav/wx-zong.html"
        self.doushi = "http://chuangshi.qq.com/bang/fav/ds-zong.html"
        self.type_url_list = [self.xuanhuan, self.wuxia, self.doushi]

    def url_text(self, url):
        r = requests.get(url=url, headers=self.headers)
        return r.text

    def get_page_info(self, html_text):
        html = etree.HTML(html_text)
        top = html.xpath("//tbody[@id='rankList']//tr[not(@class='topline')]//td//strong//text()")
        type = html.xpath("//tbody[@id='rankList']//tr[not(@class='topline')]//td[2]//text()")
        bookname = html.xpath("//tbody[@id='rankList']//tr[not(@class='topline')]//td[3]//a//text()")
        collection = html.xpath("//tbody[@id='rankList']//tr[not(@class='topline')]//td[5]//text()")
        return [top, bookname, collection, type]

    # 获取详情的url
    def get_details_url(self, html_text):
        html = etree.HTML(html_text)
        details_url_list = html.xpath("//tbody[@id='rankList']//tr[not(@class='topline')]//td[3]/a/@href")
        return details_url_list

    # 请求详情页的信息，标签和简介
    def get_con_label(self, url):
        html_text = self.url_text(url)
        html = etree.HTML(html_text)
        book_info = html.xpath("//div[@class='info']//text()")
        book_info = "".join(book_info)
        book_label = html.xpath("//div[@class='tags']//text()")[0].strip()[5:]
        if len(book_label) == 0:
            book_label = "暂无"
        else:
            book_label = book_label.strip()
        return book_info, book_label


if __name__ == '__main__':
    chuangshi = ChuangShiSpider()
    top_list, bookname_list, collection_list, info_list, label_list, type_list = [], [], [], [], [], []
    num = 0
    print("*-*-*--*-*爬取创世小说网*-*-*--*-*")
    for url in chuangshi.type_url_list:
        html_text = chuangshi.url_text(url)
        # [top, bookname, collection, type]
        page_info_list = chuangshi.get_page_info(html_text)
        details_url_list = chuangshi.get_details_url(html_text)  # 详情页链接
        book_info = []
        book_label = []
        for details_url in details_url_list:
            info, label = chuangshi.get_con_label(details_url)
            book_info.append(info)
            book_label.append(label)
            num = num + 1
            print("创世小说网第%d本小说爬取成功！" % num)
        top_list = top_list + page_info_list[0]
        bookname_list = bookname_list + page_info_list[1]
        collection_list = collection_list + page_info_list[2]
        type_list = type_list + page_info_list[3]
        info_list = info_list + book_info
        label_list = label_list + book_label
    data_dic = {
        "top": top_list,
        "bookname": bookname_list,
        "collection": collection_list,
        "info": info_list,
        "label": label_list,
        "type": type_list
    }
    df = pd.DataFrame(data_dic)
    df.to_csv("./chuangshi_data.csv", header=True, index=False)
    print("*-*-*-*--*创世小说网爬取并保存完毕*-*-*-*--*")
