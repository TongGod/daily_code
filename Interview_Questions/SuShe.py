# @Time    : 2020/9/18 16:38
# @Author  : GodWei
# @File    : SuShe.py

#  代码阅读题
# 1
def extendList(val, list=[]):
    list.append(val)
    return list


list1 = extendList(10)
list2 = extendList(123, [])
list3 = extendList("a")

print(list1)
print(list2)
print(list3)
"""
[10, 'a']
[123]
[10, 'a']
考察点：  引用的指向、默认参数
list3和list1为同一个列表，
而list2->extendList(123,[]) 给list=[]重新赋值,是一个重新的列表，
（1）当栈中出现了一个list1，list1指向了堆中的一个空列表
（2）栈中出现了一个list2，list2指向了堆中的另一个空列表，不是默认的空列表，是重新赋值的（list=[]）
（3）栈中 出现了一个list3,并没有在堆中重新建空列表，而是默认的列表，所以把"a"就添加到默认的列表中
"""


# def extendList(val,list=[]):
#     list.append(val)
#     return list
#
# list1 = extendList(10)
# print(list1)
# list2 = extendList(123,[])
# print(list2)
# list3 = extendList("a")
# print(list3)
# """
# [10]
# [123]
# [10, 'a']
# """

# 2.
def div1(x, y):
    print("%s/%s=%s" % (x, y, x / y))


def div2(x, y):
    print("%s//%s=%s" % (x, y, x // y))


div1(5, 2)
div1(5.0, 2)  # 5. 就相当于5.0
div2(5, 2)
div2(5.0, 2)
"""
5/2=2.5
5.0/2=2.5
5//2=2
5.0//2=2.0
"""

# 3.
list1 = [[]] * 5
print(list1)
list1[0].append(10)
print(list1)
list1[1].append(20)
print(list1)
list1.append(30)
print(list1)
"""
[[], [], [], [], []]
[[10], [10], [10], [10], [10]]
[[10, 20], [10, 20], [10, 20], [10, 20], [10, 20]]
[[10, 20], [10, 20], [10, 20], [10, 20], [10, 20], 30]
思路：
    在list1中存储了5个空列表(其实内存中存储的是5个同一列表地址，同一个实体),
    给其中一个小列表中添加元素，所有的小列表都会被追加
    list1[0].append(10) -> 即 存储的10到同一个地址，且有5个相同列表地址
    list1[1].append(20) -> 继续添加到列表中每个列表的1的位置，添加一个20，也是5个相同列表地址
    list1.append(30)   给最外层的列表，最后添加一个元素30

"""

# 4.
list1 = ['a', 'b', 'c', 'd']
print(list1[10:])
"""
打印结果：
[]
"""


# 5.
def func(x, l=[]):
    for i in range(x):
        l.append(i * i)
    print(l)


func(2)
func(3, [3, 2, 1])
func(3)
"""
打印结果：
[0, 1]
[3, 2, 1, 0, 1, 4]
[0, 1, 0, 1, 4]
"""


# 6.
def _add(a):
    def add(b):
        return a + b

    return add


ad = _add(1)
print(ad(1))
print(ad(2))
print(ad(3))
"""
打印结果：
2
3
4
"""


# 7.
def myFunc(a, b, c, d):
    print(a, b)


mylist = [1, 2, 3, 4]
myFunc(*mylist)  # 传的还是列表
"""
考察拆包和解包
注意 ：  如果*xxx作为实参，则将容器中的元素给形参进行赋值，
此时需要保证形参和实参的数量一致
打印结果：
1 2
"""

# 8.
str1 = "hello python"
str1.title()
print(str1)
"""
title()将每个字符串的首字母大写，但是特别注意的是
只要遇到字符串的改变得到都是新字符串，原字符串不变
要赋值给一个新的变量，再进行打印
hello python
"""


# 9.
def text(l):
    l[1] = 10


list1 = [1, 2, 3, 4]
text(list1)
print(list1)
"""
# 引用传递：如果形参发生改变，则实参也会随着发生改变
打印结果
[1, 10, 3, 4]
"""

# 10.
A0 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, }
A1 = range(10)
A2 = [i for i in A1 if i in A0]
A3 = [A0[s] for s in A0]
A4 = [i for i in A1 if i in A3]
A5 = {i: i * i for i in A1}
A6 = [[i, i * i] for i in A1]
print(A0)
print(A1)
print(A2)
print(A3)
print(A4)
print(A5)
print(A6)
"""
A2里面的条件都不满足，都不是键，即为空列表
打印结果：
{'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
range(0, 10)
[]
[1, 2, 3, 4, 5]
[1, 2, 3, 4, 5]
{0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
[[0, 0], [1, 1], [2, 4], [3, 9], [4, 16], [5, 25], [6, 36], [7, 49], [8, 64], [9, 81]]
"""