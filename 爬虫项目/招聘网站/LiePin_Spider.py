import time

import requests
from fake_useragent import UserAgent
from lxml import etree


class LiePin_Spider:
    def __init__(self):
        self.z_url = "https://www.liepin.com/"
        self.headers = {
            "User-Agent": UserAgent().random,
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Cache-Control": "max-age=0",
            "Connection": "keep-alive"
        }

    # 获取总分类
    def get_sort_url(self):
        r = requests.get(self.z_url, headers=self.headers)
        text = r.text
        html = etree.HTML(text)
        sort_url = html.xpath("//p[@class='subsite-btn clearfix']//a/@href")
        return sort_url

    def get_all_key_url(self, url_list):
        all_key_url = []  # 未拼接的url
        complete_url_list = []  # 已经拼接完整的url
        for url in url_list:
            r = requests.get(url, headers=self.headers)
            text = r.text
            html = etree.HTML(text)
            part_url = html.xpath("//ul[@class='sidebar float-left']//li//dl//dd//a/@href")
            all_key_url.append(part_url)
        # 进行拼接url
        for all_list in all_key_url:
            for i in all_list:
                complete_url_list.append(self.z_url + i)
        return complete_url_list

    # 处理爬取数据的前后空格
    def process_empt(self, unprocess_list):
        sucess_list = []
        for value in unprocess_list:
            sucess_list.append(str(value).strip())
        return sucess_list

    def get_detailed_url(self, out_url):
        a = 0
        for i in out_url:
            r = requests.get(url=i, headers=self.headers)
            text = r.text
            html = etree.HTML(text)
            unprocess_job_name = html.xpath("//div[@class='job-info']/h3/a//text()")
            unprocess_job_salary = html.xpath("//div[@class='job-info']/p//span[@class='text-warning']//text()")
            process_job_edu = html.xpath("//div[@class='job-info']/p//span[@class='edu']//text()")
            process_job_exp = html.xpath(
                "//div[@class='job-info']/p[@class='condition clearfix']//span[last()]//text()")
            process_job_area = html.xpath("//div[@class='job-info']/p/a//text()")
            process_job_time = html.xpath("//div[@class='job-info']//p[@class='time-info clearfix']/time/@title")
            process_job_company = html.xpath("//div[@class='company-info nohover']/p/a//text()")
            unprocess_job_field = html.xpath("//div[@class='company-info nohover']//p[last()]/span//text()")

            job_name = self.process_empt(unprocess_job_name)
            process_job_field = self.process_empt(unprocess_job_field)
            a = a + 1
            print("外层列表" + str(a) + "  正在爬取关键词 ：" + html.xpath("//div[@class='input-main']/input/@value")[0])
            print(job_name)
            print(unprocess_job_salary)
            print(process_job_edu)
            print(process_job_exp)
            print(process_job_area)
            print(process_job_time)
            print(process_job_company)
            print(process_job_field)

            time.sleep(2)
            break


if __name__ == '__main__':
    liepin = LiePin_Spider()
    sort_url = liepin.get_sort_url()  # 获取总的大的分类（即为最外层的分类）
    complete_url = liepin.get_all_key_url(sort_url)  # 然后获取所有最外层分类里面的小类
    liepin.get_detailed_url(complete_url)
