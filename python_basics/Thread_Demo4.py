# @Time    : 2020/11/4 17:44
# @Author  : GodWei
# @File    : Thread_Demo2.py
import threading

# 定义全局变量
g_list = []


# 添加数据
def add_data():
    for i in range(10):
        # 每循环一次就把数据添加到全局变量中
        g_list.append(i)
        print("add: ", i)


# 读取数据
def read_data():
    print("read：", g_list)


if __name__ == '__main__':
    # 创建子线程
    add_thread = threading.Thread(target=add_data)
    read_thread = threading.Thread(target=read_data)

    add_thread.start()
    add_thread.join()
    read_thread.start()

