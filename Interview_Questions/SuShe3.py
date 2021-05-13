# @Time    : 2020/9/19 17:57
# @Author  : GodWei
# @File    : SuShe3.py
"""
2.已知有字符串 "I wish you have a wonderful tomorrow"
    a. 统计出字符串中字母 "a" 出现的次数
    b. 将整个字符串倒序输出
    c. 判断这个字符串是否对称的
    d. 将字符串中每一个单词的第一个字母变成大写
"""
str1 = "I wish you have a wonderful tomorrow"

# a
# 方式一
c1 = str1.count("a")
# 方式二
c_1 = 0
for ch in str1:
    if ch == "a":
        c_1 += 1
print(c1)
print(c_1)
"""
2
2
"""

# b
# 方式一
str2 = str1[::-1]
print(str2)
# 方式二
str_2 = ""
n = len(str1) - 1
while n >= 0:
    str_2 += str1[n]
    n -= 1
print(str_2)
# 方式三
list1 = list(str1)
list1.reverse()
str__2 = "".join(list1)
print(str__2)
"""
worromot lufrednow a evah uoy hsiw I
worromot lufrednow a evah uoy hsiw I
worromot lufrednow a evah uoy hsiw I
"""

# c
if str1 == str2:
    print("对称的")
"""不对称所以不打印"""

# d
str3 = str1.title()
print(str3)
"""
I Wish You Have A Wonderful Tomorrow
"""

"""
3.在下面字典中找到年龄最大的人，并输出姓名和年龄
    person = {"li": 18, "wang": 50, "zhang": 20, "sun": 22}
"""
person = {"li": 18, "wang": 50, "zhang": 20, "sun": 22}

max_value = max(person.values())
for name, age in person.items():
    if age == max_value:
        print("姓名：%s , 年龄：%d" % (name, age))

"""
姓名：wang , 年龄：50
"""

"""
4.设计一个函数，对传入的字符串（假定字符串中只包含小写字母和空格）进行加密
    加密的规则是a变d , b变e , c变f , ······ , x 变 a , y 变 b , 空格不变，
    返回加密后的字符串
"""


def func(str1):
    # 声明一个空字符串，用于接收加密之后的新字符串
    result = ""
    for ch in str1:
        value = ord(ch)
        if 97 <= value <= 119:
            result += chr(value + 3)
        elif 120 <= value <= 122:
            result += chr(value - 23)
        else:
            result += chr(value)
    return result


print(func("abcdjei1535gef"))
"""
defgmhl1535jhi
"""

"""
5.计算字符串中所有数字的和，已知字符串中都是字母和数字
    比如传递 "12abc34def54lala" 返回 12+34+54 = 100
    比如传递 "lov240fdgj354rn235" 返回 240+354+235 = 829
"""
import re

str1 = "12abc34def54lala"
# 中括号只能匹配一位数字，大写26个字母和小写26个字母, +:加号至少能够匹配一位
list1 = re.split(r"[a-zA-Z]+", "12abc34def54lala")
for ele in list1:
    if ele == "":
        list1.remove("")
print(list1)
totall = 0
for ele in list1:
    totall += int(ele)
print(totall)
"""
['12', '34', '54']
100
"""