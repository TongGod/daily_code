# 装饰器

# 不修改函数的源代码，可以给该函数增加一个新功能

# 1. 简单的装饰器
def test():
    print("人生苦短，我用python")


# 装饰器的书写步骤
# 1.书写闭包
# 2.传参：给outter设置参数，该参数表示需要被增加的功能函数
def outter(func):
    def inner():
        # 3.调用原函数
        func()
        # 4.增加新功能
        print("PYTHON")

    # 5.将装饰之后的结果返回【方便在函数外面调用】
    return inner


# 6.然后进行调用
f = outter(test)
f()

"""
装饰器的执行顺序：
    1.f = outter(test),调用outter函数，func = test , f = inner
    2.f(),调用inner函数
    3.func(), 调用test原函数
"""


# 2.有参数的装饰器

def getAge(age):
    print(age)


# 需求：当传入的年龄为负数时，打印相反数
def outter2(func):
    def inner2(num):
        if num < 0:
            num = abs(num)
        func(num)

    return inner2


f2 = outter2(getAge)  # func = getAge   f2 = inner2
f2(-31)
"""
通过上述的操作，将边界检查的操作隔离到单独的函数中，并没有修改原函数
 给装饰器的内部函数是否需要设置参数，如果原函数有参数，并且在装饰器中
 的inner中需要对原函数的参数运算
 则建议给inner设置参数，该参数需要和原函数的参数有关
"""


# 3.使用符号@将装饰器应用于函数          @的作用：简化装饰器的调用
def outter3(func):
    def inner3(num):
        if num < 0:
            num = abs(num)
        func(num)

    return inner3


# 使用@应用装饰器
@outter3
def getAge(age):
    print(age)


# 调用
getAge(-69)

"""
@装饰器的执行的顺序
    1.@outter3: 相当于f = outter3(getAge),完成了func = getAge,
                f = inner3也就是getAge = inner3
    2.getAge(-69) : 相当于【f(-69)】,调用inner3
"""


# 4.一个装饰器修改多个函数，多个函数都没有参数
def outter4(func):
    def inner4(*args, **kwargs):  # 使用不定长参数
        func(*args, **kwargs)
        print("装饰器中的新功能")

    return inner4


@outter4
def show1():
    print("show-1")
    print("show1无参数")


@outter4
def show2(a, b):
    print("show-2")
    print('show2中的参数：', a, b)


@outter4
def show3(num1, num2, num3):
    print("show-3")
    print('show3中的参数：', num1, num2, num3)


show1()
show2(2, 3)
show3(4, 5, 6)


# 4.多个装饰器修改一个函数
def outter_1(func1):
    def inner_1(*args, **kwargs):  # 使用不定长参数
        print("inner_1内容")
        func1(*args, **kwargs)
        print("第一个装饰器-----1")

    return inner_1


def outter_2(func2):
    def inner_2(*args, **kwargs):  # 使用不定长参数
        print("inner_2内容")
        func2(*args, **kwargs)
        print("第二个装饰器-----2")

    return inner_2


def outter_3(func3):
    def inner_3(*args, **kwargs):  # 使用不定长参数
        print("inner_3内容")
        func3(*args, **kwargs)
        print("第三个装饰器-----3")

    return inner_3


@outter_1
@outter_2
@outter_3
def show_1():
    print("show_1")


show_1()
"""
    多个装饰器加载的顺序
    1.@outter_3:show_1原函数-->outter_3-->func3 = show_1原函数-->show_1指向了inner_3
    2.@outter_2:inner_3-->outter_2-->func2 = inner_3-->show_1指向了inner_2
    3.@outter_1: inner_2-->outter_1-->func1 = inner_2-->show_1最终指向了inner_1
    所以多个装饰器的执行调用过程
    show_1()-->inner_1()-->func1()-->inner_2()-->func2()-->inner_3()-->func3()-->show_1()原
"""

"""
结论：
    如果多个装饰器修饰同一个函数，
            传参：       从下往上【就近原则】
    代码的执行顺序：       从上往下
"""