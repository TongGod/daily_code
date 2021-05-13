# @Time    : 2020/9/21 18:04
# @Author  : GodWei
# @File    : datetimeDemo.py

import datetime

# 1.获取当前时间
d1 = datetime.datetime.now()
print(d1)
print(type(d1))
"""
2020-09-21 18:06:20.772943
<class 'datetime.datetime'>
"""

# 2.获取指定时间【年，月，日，时，分，秒，毫秒】
d2 = datetime.datetime(2016, 6, 6, 6, 6, 6, 6666)
print(d2)
"""
2016-06-06 06:06:06.006666
"""

# 3.字符串和datetime类型之间的转换
d3 = datetime.datetime.now()
d4 = d3.strftime("%Y/%m/%d")
print(d4)
print(type(d4))
d5 = datetime.datetime.strptime(d4,"%Y/%m/%d")
print(d5)
print(type(d5))
"""
2020/09/21
<class 'str'>
2020-09-21 00:00:00
<class 'datetime.datetime'>
"""

# 4.datetime时间对象之间可以进行减法运算
date1 = datetime.datetime(2016, 6, 6, 6, 6, 6, 6666)
date2 = datetime.datetime(2016, 6, 10, 6, 20, 20, 6666)
result = date2 - date1
print(result)
print(result.days)
print(result.seconds)
"""
4 days, 0:14:14
4
854
"""