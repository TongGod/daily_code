# @Time    : 2020/9/20 13:51
# @Author  : GodWei
# @File    : timeDemo.py
import time

'''时间的获取'''
# 1.返回当前时间的时间戳，结果为一个浮点数
t1 = time.time()
print(t1)

# 2.获取UTC的元组形式
t2 = time.gmtime()
print(t2)

# 3.获取本地时间的元组形式
t3 = time.localtime()
print(t3)

'''时间相互之间的转换'''
# 4.将时间的元组形式转换为时间戳形式
t4 = time.mktime(t3)
print(t4)

# 5.将时间的元组形式转换为字符串形式
t5 = time.asctime(t3)
print(t5)

# 6.将时间戳形式转换为字符串形式
t6 = time.ctime(t4)
print(t6)

# 7.将时间的元组形式转换为字符串形式：自定义格式
t7 = time.strftime("%Y-%m-%d", t3)
print(t7)

# 8.将时间的字符串形式转换为元组形式
# 注意：时间的字符串必须和时间的格式保持完全一致，否则报错
t8 = time.strptime("2020-2-20", "%Y-%m-%d")
print(t8)

"""
    时间戳   <----  元组  
    时间戳   ---->  字符串
    元组     <--->  字符串
"""

# 9.休眠
print("start~~~~")
# 作用： 会让代码暂停【阻塞】，当指定的时间达到之后，则会自动解除阻塞，代码继续向下执行
time.sleep(1)
print("end~~~~")

"""
    写一个装饰器，可以统计任意一个函数的执行时间
"""


def countRunTime(func):
    def inner(*args, **kwargs):
        start = time.time()
        # 调用原函数
        func()
        end = time.time()
        print("程序执行总花费了：%f秒" % (end - start))

    return inner()


@countRunTime
def testFunc():
    print("program ~~~~  strat")
    time.sleep(1)
    print("program ~~~   end ")


"""
    有一个时间字符串，如：1999/9/9,输出三天之后的日期1999/9/12
"""

str1 = "1999/9/9"
# 将时间的字符串转换为元组
time1 = time.strptime(str1, "%Y/%m/%d")
# 将时间的元组形式转换为时间戳
time2 = time.mktime(time1)
# 进行加法运算
time3 = time2 + 3 * 24 * 3600
# 将时间戳转换为时间元组
time4 = time.localtime(time3)
# 将时间元组转化为字符串格式
time5 = time.strftime("%Y/%m/%d", time4)
print(time5)


# 可以简化所有的代码
time_1 = time.strftime("%Y/%m/%d", time.localtime(time.mktime(time.strptime(str1, "%Y/%m/%d")) + 3 * 24 * 3600))
print(time_1)