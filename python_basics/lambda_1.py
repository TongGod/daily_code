# 匿名函数
def text(x, y):
    result = x + y


lambda x, y: x + y
"""
    1.def text(x, y) 是def的声明部分，return x+y 是实现部分
      lambda x,y是声明部分，x + y是实现部分
    2.lambda 是对def标准形式定义函数的简化，因为只有一行代码
    3.lambda 表示匿名函数，所以默认参数，关键字参数以及不定长参数都可以正常使用
    4.lambda 仅仅是一个表达式，而不是一个语句
    5.lambda 的主体部分是一个单个的语句，而不是代码块
    6.lambda 拥有自己的命名空间，不能访问自有参数列表之外的或者全局变量
    7.lambda 只能实现简单的逻辑，如果逻辑复杂且代码量较大，则不建议使用lambda，
       降低代码的可读性，为后期的代码维护增加困难
    8.在非多次调用函数的情况下，lambda简单而且性能较高
"""


