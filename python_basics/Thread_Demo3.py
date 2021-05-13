# @Time    : 2020/11/4 17:44
# @Author  : GodWei
# @File    : Thread_Demo2.py
import threading
import time


def task():
    while True:
        print("子线程任务执行中***")
        time.sleep(0.2)


if __name__ == '__main__':
    # 创建子线程
    # daemon=True 表示创建的子线程守护主线程，主线程退出子线程直接销毁
    sub_thread = threading.Thread(target=task)
    sub_thread.setDaemon(True)
    sub_thread.start()

    # 主线程延迟执行1秒
    time.sleep(1)
    print("主线程over")
