# @Time    : 2020/8/30 22:55
# @Author  : GodWei
# @File    : sortedDemo.py
# 普通排序，默认升序
list1 = [34, 6, 4, 6, 2, 5, 1, 52561, 65]
print(list1)
list1.sort()
print(list1)

list1 = [34, 6, 4, 6, 2, 5, 1, 52561, 65]
print(list1)
list2 = sorted(list1)
print(list2)

# 降序排序
list1 = [34, 6, 4, 6, 2, 5, 1, 52561, 65]
print(list1)
list1.sort(reverse=True)
print(list1)

list1 = [34, 6, 4, 6, 2, 5, 1, 52561, 65]
print(list1)
list3 = sorted(list1, reverse=True)
print(list3)

"""
    可以自定义排序
    根据数字元素的绝对值排序
"""
list4 = [-34, 54, 69, -42, 12, 341, 10, 98, -9]
list4.sort(key=abs)
print(list4)

list4 = [-34, 54, 69, -42, 12, 341, 10, 98, -9]
list5 = sorted(list4, key=abs)
print(list5)


def func1(s):
    return int(s)


list_1 = ["345", "26", "789", "450", "12", "1"]
list_2 = sorted(list_1, key=func1)
print(list_2)

list_3 = ["sdfas", "evasdqsd", "dfea", "bsfe", "csfge", "cca"]
list_4 = sorted(list_3)  # 根据每个字符进行排序，依次比较下去
print(list_4)

list_5 = sorted(list_4, key=len)  # 按照长度
print(list_5)
