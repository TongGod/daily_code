# 1
def test():
    print("test")


# 打印出函数，和函数的类型
print(test, type(test))
test()  # 调用函数
'''
    匿名函数不需要使用return进行值的返回，只需要将结果书写在函数体的部分，
    值会被自动返回
'''
r1 = lambda: True
print(r1, type(r1))
print(r1())


# 2.匿名函数的函数体可以直接写打印语句，但是返回值则为None
def test1():
    print("test1")


print(test1())
r2 = lambda: print("lambda_print")
print(r2())

# 3. 匿名函数的参数
r3 = lambda x: x ** 3  # 传递一个x,然后给x三次方，并返回
print(r3(2))  # 打印2的三次方

r4 = lambda x, y: x + y  # 传递一个x和y,然后给相加，并返回
print(r4(3, 5))  # 打印3+5

# 4. 匿名函数可以使用默认参数，关键字参数，不定长参数
r5 = lambda x, y=5: x + y  # 默认参数
print(r5(2))
print(r5(2, 10))
print(r5(x=8, y=9))  # 关键字参数

r6 = lambda *a: a  # 不定长参数
print(r6(1, 2, 3, 4, 5, 6))


# 需求：比较两个数的大小，返回较大的数
# 1.用正常的方式
def compare(num1, num2):
    if num1 >= num2:
        return num1
    else:
        return num2


print("传统的方式：", compare(9, 6))
# 2.用匿名函数
r7 = lambda num1, num2: num1 if (num1 >= num2) else num2
print("使用匿名函数：", r7(9, 3))
# 3.使用匿名函数另一种方式，直接赋值
r8 = (lambda num1, num2: num1 if (num1 >= num2) else num2)(9, 6)
print("使用匿名函数另一种方式：", r8)
