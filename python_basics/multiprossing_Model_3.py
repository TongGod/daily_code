# @Time    : 2020/10/29 21:42
# @Author  : GodWei
# @File    : multiprossing_Model_3.py

import multiprocessing


# 显示信息的任务
def show_info(name, age):
    print(name, age)


# # 以元组方式传参，元组里面的元素顺序要和函数的参数顺序保持一致
# sub_process = multiprocessing.Process(target=show_info, args=("李四", 20))

# 以字典方式传参，字典里面的key要和函数里面的参数名保持一致，没有顺序要求
sub_process = multiprocessing.Process(target=show_info, kwargs={"age": 20, "name": "王五"})

if __name__ == '__main__':
    sub_process.start()

    sub_process.terminate()
