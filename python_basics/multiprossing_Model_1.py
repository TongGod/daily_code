# @Time    : 2020/10/27 22:42
# @Author  : GodWei
# @File    : multiprossing_Model_1.py.py

import time
import multiprocessing

# 跳舞任务
def dance():
    for i in range(3):
        print("跳舞中...")
        time.sleep(0.2)

# 唱歌任务
def sing():
    for i in range(3):
        print("唱歌中...")
        time.sleep(0.2)

# 创建子进程
dance_process = multiprocessing.Process(target=dance)
sing_process = multiprocessing.Process(target=sing)

# 启动进程执行对应的任务
if __name__ == '__main__':
    dance_process.start()
    sing_process.start()
