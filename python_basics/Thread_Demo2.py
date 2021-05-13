# @Time    : 2020/11/4 17:44
# @Author  : GodWei
# @File    : Thread_Demo2.py
import threading
import time

def task():
    time.sleep(0.2)
    # 获取当前线程
    print(threading.current_thread())


if __name__ == '__main__':
    for i in range(20):
        # 每循环一次创建一个子线程
        sub_thread = threading.Thread(target=task)
        # 启动子线程
        sub_thread.start()