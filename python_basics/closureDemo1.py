# 1.函数的简单用法
def func1():
    num1 = 10
    print("func--1")


def func2():
    # 问题： 在一个函数中无法访问另一个函数的变量
    # print(num1)
    print("func--2")


# 2.闭包的使用
def func3(a):
    num2 = 66
    print("func--3")

    def func4():
        """
            当定义了闭包之后，在内部函数中可以直接访问外部函数的变量
            a和num2 被称为自由变量，也被称为临时变量
        """
        print(num2)  # 打印外部函数的变量
        print(a)  # 打印外部函数的参数
        print("func--4")

    '''外部函数的返回值是内部函数的引用'''
    return func4()


func3(a=20)  # 调用，并且传递一个参数


# 3. 内部函数可以根据需求设置返回值
def outter(a):
    def inner(b):
        return a + b

    return inner


f = outter(33)
result = f(20)
print(result)
