# @Time    : 2020/11/11 20:34
# @Author  : GodWei
# @File    : shui_xian_hua.py

for i in range(100, 999):
    a = i // 100
    b = (i % 100) // 10
    c = i % 10
    if i == a ** 3 + b ** 3 + c ** 3:
        print(i)
