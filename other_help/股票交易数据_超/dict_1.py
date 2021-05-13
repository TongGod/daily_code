# @Time    : 2020/8/26 16:28
# @Author  : GodWei
# @File    : dict_1
# @Software: PyCharm
import pandas as pd
import numpy as np
import datetime
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']

data = {
    "日期": [
        '2020-01-01', '2020-01-02', '2020-01-03', '2020-01-06',
        '2020-01-07', '2020-01-08', '2020-01-09', '2020-01-10',
        '2020-01-13', '2020-01-14',
    ],
    "开盘价（元）": [12.32, 12.27, 12.25, 12.26, 12.29,
               12.21, 12.46, 12.41, 12.4, 12.36
               ],
    "收盘价（元）": [12.37, 12.34, 12.32, 12.29, 12.24,
               12.28, 12.2, 12.42, 12.41, 12.4
               ]
}

df = pd.DataFrame(data)

# 第一小题
dict_1 = {}
for i in range(0, len(df)):
    dict_1[df["日期"][i]] = df["收盘价（元）"][i]

# 第二小题
dict_1["2020-01-15"] = 12.5

# 第三小题
assumed_date = '2020-01-12'
assumed_datetime = datetime.datetime.strptime(str(assumed_date), '%Y-%m-%d')
df['日期'] = df['日期'].astype('datetime64')
df['日期'] = [df['日期'][i].date() for i in range(0, len(df))]
fit_time = []
num = 1
while True:
    num = num + 1
    time_before = (assumed_datetime - datetime.timedelta(days=num)).strftime("%Y-%m-%d %H:%M:%S")
    time_before_new = datetime.date(*map(int, time_before.split(" ")[0].split('-')))
    if time_before_new in df['日期'].tolist():
        fit_time.append(time_before_new)
    if len(fit_time) == 4:
        break
print("1月12日四天前的收盘价:")
for i in fit_time:
    index = df[df['日期'] == i].index.tolist()[0]
    print(df["收盘价（元）"][index])

# 第四个小题
df_index = int(df[df['日期'] == datetime.date(*map(int, '2020-01-13'.split('-')))]['收盘价（元）'].index.tolist()[0])
df.loc[df_index, "收盘价（元）"] = 12.43

# 第七个小题
time_x = []
o_y = []
c_y = []
time_x_tick = []
for i in range(0, len(df)):
    if df['日期'][i].day <= 15:
        time_x.append(str(df['日期'][i]))
        time_x_tick.append(str(df['日期'][i])[0:4] + "\n" + str(df['日期'][i])[5::])
        o_y.append(df["开盘价（元）"][i])
        c_y.append(df["收盘价（元）"][i])

plt.plot(time_x, o_y)
plt.plot(time_x, c_y)
plt.ylabel('价格（元）')
plt.xlabel('时间')
plt.xticks(time_x,time_x_tick, rotation=60)
plt.xlabel('日期')
plt.title("2020年1月前半个月的两种价格")
plt.grid()
plt.show()


