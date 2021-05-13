#  列表生成式
# 方式一：使用range()和list()函数
list1 = list(range(1, 10))
print(list1)

# 方式二：循环，添加到列表中
list2 = []
for i in range(1, 10):
    list2.append(i)
print(list2)

"""
通过range生成的列表，缺点：生成的列表规律性较强，其中的元素相互之间的差值是相等的【step】
"""

# -------------
# 方式一
list3 = []
for i in range(1, 10):
    list3.append(i ** 2)
print(list3)

# 方式二
list4 = [i ** 2 for i in range(1, 10) if i % 2 == 1]
print(list4)

# 需求：生成一个列表，列表中的元素为1-100以内3的倍数
# 方式一：传统方式
list5 = []
for i in range(1, 100):
    if i % 3 == 0:
        list5.append(i)
print(list5)
# 方式二：使用列表生成式
list6 = [i for i in range(1, 100) if i % 3 == 0]
print(list6)

# 方式一：传统方式
list7 = []
for i in "abc":
    for j in "xyz":
        list7.append(i + j)
print(list7)
# 方式二：使用列表生成式
list8 = [i + j for i in "abc" for j in "xyz"]
print(list8)

dict1 = {'a': 10, 'b': 20, 'c': 30}
# 方式一：传统方式
list9 = []
for key, value in dict1.items():
    list9.append(str(key) + str(value))
print(list9)
# 方式二：使用列表生成式
list10 = [key + str(value) for key, value in dict1.items()]
print(list10)

"""
    注意：列表生成式相比较普通列表的生成式，比较简洁，
        但是只能实现简单的逻辑，否则代码的可读性降低
"""

list_1 = ['hello', 10, 'Abc', 'asBd', True]
# 方式一：
newlist_1 = []
for s in list_1:
    if isinstance(s, str):  # isinstance()来判断是不是str类型
        newlist_1.append(s.upper())
print(newlist_1)
# 方式二：
newlist_2 = [s.upper() for s in list_1 if isinstance(s, str)]
print(newlist_2)
