# @Time    : 2020/10/28 12:19
# @Author  : GodWei
# @File    : multiprossing_Model_2.py
import os
import multiprocessing
import time


# 获取进程编号
def dance():
    # 获取当前进程（子进程）的编号
    dance_process_id = os.getpid()
    # 获取当前进程对象，查看当前代码是由那个进程执行：
    print("dance_process_id:", dance_process_id, multiprocessing.current_process())
    # 获取当前进程的父进程编号
    dance_process_parent_id = os.getppid()
    print("dance_process的父进程编号是：", dance_process_parent_id)

    for i in range(3):
        print("跳舞中...")
        time.sleep(0.2)
        # 根据进程编号强制杀死指定进程
        os.kill(dance_process_id, 9)


# 获取进程编号
def sing():
    # 获取当前进程（子进程）的编号
    sing_process_id = os.getpid()
    # 获取当前进程对象，查看当前代码是由那个进程执行：
    print("sing_process_id:", sing_process_id, multiprocessing.current_process())
    # 获取当前进程的父进程编号
    sing_process_parent_id = os.getppid()
    print("sing_process的父进程编号是：", sing_process_parent_id)

    for i in range(3):
        print("唱歌中...")
        time.sleep(0.2)
        # 根据进程编号强制杀死指定进程
        os.kill(sing_process_id, 9)




# 启动进程
if __name__ == '__main__':
    # 获取当前进程（主进程）的编号
    main_process_id = os.getpid()
    print("main_process_id:", main_process_id, multiprocessing.current_process())

    # 创建子进程
    dance_process = multiprocessing.Process(target=dance, name="dance_process")
    print("dance_process:", dance_process)
    sing_process = multiprocessing.Process(target=sing, name="sing_process")
    print("sing_process:", dance_process)

    # 启动进程
    dance_process.start()
    sing_process.start()
