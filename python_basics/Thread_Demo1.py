# @Time    : 2020/11/4 17:22
# @Author  : GodWei
# @File    : Thread_Demo1.py
import threading


def eat(name, number):
    print("eating :%s number :%d" % (name, number))


def watch(name, type):
    print("watch : %s type：%s" % (name, type))


if __name__ == '__main__':
    eat_thread = threading.Thread(target=eat, kwargs={"name": "爆米花", "number": 1})
    watch_thread = threading.Thread(target=watch, kwargs={"name": "电影", "type": "科幻"})

    eat_thread.start()
    watch_thread.start()


