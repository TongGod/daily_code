# @Time    : 2021/2/2 19:23
# @Author  : GodWei
# @File    : demo01.py
import redis

if __name__ == '__main__':

    try:
        r = redis.Redis()
    except Exception as e:
        print(e)

    r.set("name", 'tong')
    name = r.get("name").decode()
    print(name)
#  192.168.1.11