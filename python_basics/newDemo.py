# @Time    : 2020/9/21 21:05
# @Author  : GodWei
# @File    : newDemo.py

#  1. 只定义init
class Check1:
    # 构造函数
    # 1.init:self表示的当前类的实例【对象】
    def __init__(self):
        print("__init__函数被调用了")


c1 = Check1()
print(type(c1))
"""
__init__函数被调用了
<class '__main__.Check1'>
"""


class Check2:
    # 构造函数
    # 1.init:self表示的当前类的实例【对象】
    def __init__(self):
        print("__init__函数被调用了")

    # 2.new： cls 表示的当前类
    def __new__(cls, *args, **kwargs):
        print("__new__被调用了")
        '''创建对象'''
        return super(Check2, cls).__new__(cls, *args, **kwargs)


c2 = Check2()
print(type(c2))
"""
__new__被调用了
__init__函数被调用了
<class '__main__.Check2'>
"""

"""
    对照代码和打印结果可知
    如果类中只定义了init, 则创建对象的时候默认第一个调用init函数
    如果类中同时定义了init和new,则创建对象的时候只会调用new函数
    
    注意：
        一般情况下，使用init较多，如果使用了new函数，
            那么则不要使用init【如果要使用init，则init不能设置参数】
    
    实际上的，是先调用new,然后再调用init
"""
