# @Time    : 2021/3/3 8:32
# @Author  : GodWei
# @File    : cookie不变测试.py
# -*- coding: utf-8 -*-

"""
加载cookies文件，使用requests库爬取数据并动态更新cookies，可以使cookies不失效
"""

import requests
from fake_useragent import UserAgent
from requests import utils


def generate_headers(url):
    ua = UserAgent()
    headers = {
        "User-Agent": ua.random,
        "Content-Type": "text/html;charset=GBK",
        "Pragma": "no-cache",
        "Host": "app1.nmpa.gov.cn",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Cache-Control": "max-age=0",
        "Connection": "keep-alive",
        "Referer": "http://app1.nmpa.gov.cn/data_nmpa/face3/base.jsp?tableId=21&tableName=TABLE21&title=%D2%BD%C1%C6%C6"
                   "%F7%D0%B5%B1%EA%D7%BC%C4%BF%C2%BC&bcId=152904437880111023387499337007",
    }
    req = requests.get(url, headers=headers)
    cookies = requests.utils.dict_from_cookiejar(req.cookies)
    print(cookies)
    for key in cookies.keys():
        print(key, cookies.get(key))



    headers_medical = {
        "User-Agent": ua.random,
        "Content-Type": "text/html;charset=GBK",
        "Pragma": "no-cache",
        "Host": "app1.nmpa.gov.cn",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Cache-Control": "max-age=0",
        "Connection": "keep-alive",
        "Referer": "http://app1.nmpa.gov.cn/data_nmpa/face3/base.jsp?tableId=21&tableName=TABLE21&title=%D2%BD%C1%C6%C6"
                   "%F7%D0%B5%B1%EA%D7%BC%C4%BF%C2%BC&bcId=152904437880111023387499337007",
        "Cookie": cookies
    }
    return headers_medical


# 请求网页
def get_html(url, headers):
    req = requests.get(url, headers=headers)
    return req.text


if __name__ == '__main__':
    # 医疗器械标准目录
    standard_catalogue_url = "http://app1.nmpa.gov.cn/data_nmpa/face3/base.jsp?tableId=21&tableName=TABLE21&title=%D2" \
                             "%BD%C1" \
                             "%C6%C6%F7%D0%B5%B1%EA%D7%BC%C4%BF%C2%BC&bcId=152904437880111023387499337007&CbSlDlH0" \
                             "=qGcsrGqfE1lfE1lfEYBsm6VWzW8HQPivXcaogBDfGU0qqcl "
    print(get_html(url=standard_catalogue_url,headers=generate_headers(standard_catalogue_url)))