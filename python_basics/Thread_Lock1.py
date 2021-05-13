# @Time    : 2020/11/4 17:22
# @Author  : GodWei
# @File    : Thread_Demo1.py
# 使用互斥锁完成2个线程对同一全局变量各加100万次的操作，而不会出现问题
import threading

# 全局变量
g_num = 0

# 创建互斥锁
lock = threading.Lock()

# 循环100万次执行的任务
def task1():
    # 表示要声明修改全局变量的内存地址
    global g_num

    # 上锁
    lock.acquire()

    # 每循环一次给全局变量加一
    for i in range(1000000):
        g_num += 1

    # 释放锁
    lock.release()
    print("task1: ", g_num)

# 循环100万次执行的任务
def task2():
    # 表示要声明修改全局变量的内存地址
    global g_num

    # 上锁
    lock.acquire()

    # 每循环一次给全局变量加一
    for i in range(1000000):
        g_num += 1

    # 释放锁
    lock.release()

    print("task2: ", g_num)

if __name__ == '__main__':
    first_thread = threading.Thread(target=task1)
    second_thread = threading.Thread(target=task1)

    first_thread.start()
    second_thread.start()
