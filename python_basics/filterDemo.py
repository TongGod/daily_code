# @Time    : 2020/8/30 22:09
# @Author  : GodWei
# @File    : filterDemo.py

list1 = [45, 163, 58, 8, 48, 16, 42, 91, 39]


def func1(num):
    if num % 2 == 0:
        return True
    return False


result1 = filter(func1, list1)
print(list(result1))

data = [
    ["姓名", "年龄", "爱好"],
    ["Tom", 18, "唱歌"],
    ["Bob", 12, "跳舞"],
    ["Lisa", 19, "无"],
]


def func2(v):
    v = str(v)
    if v == "无":
        return False
    return True


after_data = []
for d in data:
    result2 = filter(func2, d)
    after_data.append(list(result2))
print(after_data)