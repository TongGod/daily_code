# @Time    : 2020/8/29 19:44
# @Author  : GodWei
# @File    : reduceDemo.py

from functools import reduce

list1 = [1, 2, 3, 4, 5]


# 方式一
def add(x, y):
    return x + y


result1 = reduce(add, list1)
print(result1)
print(type(result1))

# 方式二
result2 = reduce(lambda x, y: x + y, list1)
print(result2)

list2 = [1, 2, 3, 4, 5]


# 方式一
def func1(x, y):
    return x * 10 + y


result3 = reduce(func1, list2)
print(result3)
print(type(result3))

# 方式二
result4 = reduce(lambda x, y: x * 10 + y, list2)
print(result4)


def func_1(n):
    digits = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5,
              "6": 6, "7": 7, "8": 8, "9": 9}

    return digits[n]


str_num = "266589"
# 找到每个str对应的数字
r1 = map(func_1, str_num)


# 组成数字
def func_2(x, y):
    return x * 10 + y


r2 = reduce(func_2, r1)
print("转换之前为：", str_num, "，类型：", type(str_num))
print("转换之后为：", r2, "，类型：", type(r2))
