# @Time    : 2020/9/18 22:55
# @Author  : GodWei
# @File    : SuShe2.py

"""
1.编写程序，已知程序中列表 ll = [2, 546, 73, 11, 66, 235, 73, 5, 89] 封装不同的函数，实现下面功能
    a.输出列表中所有的质数。（质数是只能被1和它本身整除的数）
    b.删除列表中的重复元素
    c.使用已知列表，通过列表生成式生成一个新的列表，其中的元素全部为偶数
    d.利用冒泡排序的方式对列表中的元素进行降序排序
    e.请找出列表中任意两个元素相加等于100的元素集合，生成新的列表，例如[(73,27),(95,5)]
"""
ll = [2, 546, 73, 11, 66, 235, 73, 5, 89]
# a
for num in ll:
    if num < 2:
        print("%d不是质数" % num)
    else:
        result = True
        for i in range(2, num):
            if num % i == 0:
                result = False
                break
        if result:
            print("%d是质数" % num)
        else:
            print("%d不是质数" % num)
"""
打印结果：
2是质数
546不是质数
73是质数
11是质数
66不是质数
235不是质数
73是质数
5是质数
89是质数
"""
# b
# 方式一
l2 = list(set(ll))
# 这句代码让sort()方法按照ll列表中索引顺序进行排列。
# 因为set函数会改变列表中的默认的顺序
l2.sort(key=ll.index)
# 方式二
l_2 = []
for num in ll:
    if num not in l_2:
        l_2.append(num)
print(l2)
print(l_2)
"""
打印结果：
[2, 546, 73, 11, 66, 235, 5, 89]
[2, 546, 73, 11, 66, 235, 5, 89]
"""
# c
l3 = [num for num in ll if num % 2 == 0]
print(l3)
"""
打印结果：
[2, 546, 66]
"""
# d
# 冒泡排序：相邻下标对应的元素进行比较
for i in range(0, len(ll) - 1):
    for j in range(0, len(ll) - i - 1):
        if ll[j] < ll[j + 1]:
            ll[j], ll[j + 1] = ll[j + 1], ll[j]

print(ll)
"""
打印结果：
[546, 235, 89, 73, 73, 66, 11, 5, 2]
"""
# e
l4 = []
for num1 in ll:
    for num2 in ll:
        if num1 + num2 == 100:
            l4.append((num1, num2))
print(l4)
"""
打印结果：
[(89, 11), (11, 89)]
"""


