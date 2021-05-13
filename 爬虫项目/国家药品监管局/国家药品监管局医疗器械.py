# @Time    : 2021/1/22 15:49
# @Author  : GodWei
# @File    : 国家药品监管局医疗器械.py

import requests
import re
from lxml import etree
from create_cookie import get_cookie

# 医疗器械标准目录
standard_catalogue = "http://app1.nmpa.gov.cn/data_nmpa/face3/base.jsp?tableId=21&tableName=TABLE21&title=%D2%BD%C1" \
                     "%C6%C6%F7%D0%B5%B1%EA%D7%BC%C4%BF%C2%BC&bcId=152904437880111023387499337007&CbSlDlH0" \
                     "=qGcsrGqfE1lfE1lfEYBsm6VWzW8HQPivXcaogBDfGU0qqcl "


# 读取本地cookie文件
def read_cookie():
    with open("./cookie.txt") as f:
        cookie = f.read()
    return cookie

# 读取要爬去的url列表



class Medical_Spider:
    def __init__(self):
        # 模拟请求头
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/70.0.3538.110 Mobile Safari/537.36 ",
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
            "Cookie": get_cookie()
        }
        self.standard_catalogue = "http://app1.nmpa.gov.cn/data_nmpa/face3/base.jsp?tableId=21&tableName=TABLE21&title=%D2%BD%C1" \
                                  "%C6%C6%F7%D0%B5%B1%EA%D7%BC%C4%BF%C2%BC&bcId=152904437880111023387499337007&CbSlDlH0" \
                                  "=qGcsrGqfE1lfE1lfEYBsm6VWzW8HQPivXcaogBDfGU0qqcl "
        self.testing_center_url = "http://app1.nmpa.gov.cn/data_nmpa/face3/base.jsp?tableId=18&tableName=TABLE21" \
                                  "&title=%D2%BD%C1%C6%C6%F7%D0%B5%B1%EA%D7%BC%C4%BF%C2%BC&bcId" \
                                  "=152904437880111023387499337007&CbSlDlH0=qActcGqkqaWkqaWkqTBsmdV0o1mqi1pCUZXbAfts_xqqqqW "

    # 请求网址
    def get_response(self):
        response = requests.get(url=self.testing_center_url, headers=self.headers)
        return response.text

    # 医疗器械标准目录
    #def


if __name__ == '__main__':
    cookie = read_cookie()
    medical = Medical_Spider()
    html_text = medical.get_response()
    print(html_text)
