# @Time    : 2020/8/29 17:13
# @Author  : GodWei
# @File    : mapDemo.py

# 生成一个序列，序列中的元素为1,4,9,16,25
def func1(x):
    return x ** 2


result_1 = map(func1, range(1, 6))
print(result_1, type(result_1))
print(list(result_1))
"""
    注意：
        1.fn函数有且只能有一个函数
        2.需要设置返回值，如果没有返回值，最终生成的新的序列中的元素默认为None
"""

# 方式二
result_2 = map(lambda x: x ** 2, range(1, 6))
print(list(result_2))
# 也可以写一块
result_3 = list(map(lambda x: x ** 2, range(1, 6)))
print(result_3)


# 在map中可以使用多个序列
# 方式一
def add(x, y):
    return x + y


result_4 = map(add, [1, 2, 3], [4, 5, 6])
print(list(result_4))

# 方式二
result_5 = map(lambda x, y: x + y, [1, 2, 3], [4, 5, 6])
print(list(result_5))

# 将列表中每个整型元素转换为字符串类型
list_1 = [1, 2, 3, 4, 5]
print("转换前：", list_1)
result_6 = map(str, list_1)
print("转换后：", list(result_6))

