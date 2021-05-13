# @Time    : 2021/3/16 12:53
# @Author  : GodWei
# @File    : test.py

import requests
from fake_useragent import UserAgent

ua = UserAgent()
url = "https://www.liepin.com/zhaopin/?compkind=&dqs=&pubTime=&pageSize=40&salary=&compTag=&sortFlag=&degradeFlag=0&compIds=&subIndustry=&jobKind=&industries=&compscale=&key=java&siTag=k_cloHQj_hyIn0SLM9IfRg~fA9rXquZc5IkJpXC-Ycixw&d_sfrom=search_industry&d_ckId=783c398f806ddbec4324f3b991fa6422&d_curPage=2&d_pageSize=40&d_headId=783c398f806ddbec4324f3b991fa6422&curPage=0"
headers = {
    "User-Agent": ua.random,
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cache-Control": "max-age=0",
    "Connection": "keep-alive"
}

r = requests.get(url, headers=headers)
print(r.text)
