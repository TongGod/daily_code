# @Time    : 2020/11/4 20:50
# @Author  : GodWei
# @File    : Thread_Lock2.py
# 需求： 多线程同时根据下标在列表中取值，要保证同一时刻只能有一个线程取值
import threading

# 创建锁
lock = threading.Lock()


def get_value(index):
    # 上锁
    lock.acquire()

    my_list = [0, 1, 2]
    # 判断下标是否越界
    if index >= len(my_list):
        print("下标越界：", index)
        '''
            如果加上下方代码就不会造成死锁，要把锁给释放掉
            取值不成功，也需要释放互斥锁，不要影响后面的线程去取值
            需要在合适的地方进行释放锁，防止死锁    
            lock.release()        
        '''
        # 这块直接返回了，不执行后面的代码了
        return

        # 根据下标取值
    value = my_list[index]
    print(value)

    # 释放锁
    lock.release()


if __name__ == '__main__':
    for i in range(10):
        sub_thread = threading.Thread(target=get_value, args=(i,))
        sub_thread.start()