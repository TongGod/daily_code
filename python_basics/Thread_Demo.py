# @Time    : 2020/11/2 11:09
# @Author  : GodWei
# @File    : Thread_Demo.py

# 导入线程模块
import threading
import time

def eat_candy():
    print("--正在吃糖果--")
    print(threading.current_thread())
    time.sleep(1)

if __name__ == '__main__':
    for i in range(5):
        t = threading.Thread(target=eat_candy)  # 给target传入函数的名字
        print(threading.current_thread())
        # 生成一个实例对象 t
        t.start()   # 启动线程，即让线程开始执行

