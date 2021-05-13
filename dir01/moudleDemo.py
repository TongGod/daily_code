# @Time    : 2020/9/20 9:56
# @Author  : GodWei
# @File    : moudleDemo.py

"""
    跨文件访问变量或者调用函数，则需要指明函数或者变量的来源，
    使用关键字import,格式  import  模块名
    自定义一个py文件，其实就是一个模块，只不过该模块是自定义的
"""
import aaa.moudle01
import bbb.moudle01
"""
1.书写模块的名称需要注意模块的路径【相对路径，默认的参照路径是当前工程的路径】
2.模块的书写格式：包1...包n.文件名
3.import的作用：表示将指定路径下的指定模块中的内容从头到尾加载一遍
"""

# 访问模块中的变量和调用函数
print(aaa.moudle01.str1)
aaa.moudle01.func()

print(bbb.moudle01.str1)
bbb.moudle01.func()


"""
打印结果：
aaa~~~start
aaa~~~middle
aaa~~~end
aaa
hello~~~aaa
bbb
hello~~~bbb
"""