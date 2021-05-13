from fake_useragent import UserAgent
import requests
from lxml import etree
import pandas as pd


class MediaSpider:
    def __init__(self):
        self.headers = {
            "User-Agent": UserAgent().random,
            "Host": "www.hbfu.edu.cn"
        }

    def get_html_text(self, url):
        r = requests.get(url, headers=self.headers)
        return r.text

    def get_media_url_list(self, text):
        html = etree.HTML(text)
        media_context = html.xpath("//ul[@id='xywlList']//li/a/text()")
        media_url = html.xpath("//ul[@id='xywlList']//li/a/@href")
        media_url_list = []
        for i in media_url:
            media_url_list.append("https://www.hbfu.edu.cn/" + i)
        media_date = html.xpath("//ul[@id='xywlList']//span//text()")
        return [media_context, media_url_list, media_date]

    def save_csv(self, data):
        dic = {
            "info": data[0],
            "url": data[1],
            "date": data[2]
        }

        df = pd.DataFrame(dic)
        df.to_csv('./media.csv', header=True, index=False)


if __name__ == '__main__':
    get_url = "https://www.hbfu.edu.cn/"
    media = MediaSpider()
    media_text = media.get_html_text(get_url)
    print("数据爬取成功！")
    data = media.get_media_url_list(media_text)
    media.save_csv(data=data)
    print("数据保存成功！")
