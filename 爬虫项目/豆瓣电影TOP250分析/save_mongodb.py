# coding=utf-8

import xlrd
import json
from pymongo import MongoClient

# 连接数据库
client = MongoClient('localhost', 27017)
db = client.douban
account = db.movie_model

data = xlrd.open_workbook('douban_Top250.xls')
table = data.sheets()[0]
# 读取excel第一行数据作为存入mongodb的字段名
rowstag = table.row_values(0)
nrows = table.nrows
returnData = {}
for i in range(1, nrows):
    # 将字段名和excel数据存储为字典形式，并转换为json格式
    returnData[i] = json.dumps(dict(zip(rowstag, table.row_values(i))))
    # 通过编解码还原数据
    returnData[i] = json.loads(returnData[i])
    account.insert_one(returnData[i])
print("数据保存到MongoDB数据库中成功！！！")
