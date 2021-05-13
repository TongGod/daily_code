# 函数的递归
# def test():
#     print("PYTHON")
#     test()
# test()

# 报一个数，输出在斐波那契数列中对应的数
# 如： 报10(即第十个数字)，输出55
"""
斐波那契数列
 1  1  2  3  5  8  13  21  34  55  ....
"""

num = 0


def f(n):
    global num
    num = num + 1

    if n == 1 or n == 2:
        return 1
    else:
        return f(n - 1) + f(n - 2)


r = f(10)  # 第十个位置上的斐波那契数列的数
print(r)
print("循环总次数：", num)


# 用递归实现求某个数的累加整数和
def add_1(n):
    if n == 1:
        return 1
    else:
        return add_1(n - 1) + n


result_1 = add_1(100)
print(result_1)


# 用递归实现求某个数的阶乘
def mul_1(n):
    if n == 1:
        return 1
    else:
        return mul_1(n - 1) * n


result_2 = mul_1(5)
print(result_2)
