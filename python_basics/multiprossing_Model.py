# @Time    : 2020/10/27 22:42
# @Author  : GodWei
# @File    : multiprossing_Model.py

import multiprocessing
import time


def test1():
    for i in range(3):
        print("----1----")
        time.sleep(1)


def test2():
    for i in range(3):
        print("----2----")
        time.sleep(1)


def main():

    p1 = multiprocessing.Process(target=test1)
    #
    p2 = multiprocessing.Process(target=test2)
    '''调用start(),创建了一个子进程'''
    p1.start()   # 主进程有什么，子进程就有什么
    p2.start()

if __name__ == '__main__':
    main()