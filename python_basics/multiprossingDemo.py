# @Time    : 2020/9/22 15:47
# @Author  : GodWei
# @File    : multiprossingDemo.py

import numpy as np
import multiprocessing as mp

# RandomState()是一个伪随机数生成器
np.random.RandomState(100)
# 0, 10 ： 生成0到10的随机整数
# size=[200000, 5]  即生成200000行，一列的 ndarray(二维矩阵的形式，每个里面5个元素)
arr = np.random.randint(0, 10, size=[200000, 5])
data = arr.tolist()  # 将numpy.ndarray 转化为list
# 因为是随机的，所以每次的数字不确定
data = data[:5]
print("数据为：", data)

"""不使用并行处理"""


def howmany_within_range(row, minimum, maximum):
    count = 0
    for n in row:
        if minimum <= n <= maximum:
            count += 1
    return count


result = []
for row in data:
    result.append(howmany_within_range(row, minimum=4, maximum=8))
print("给定数值范围中的元素个数：", result)
"""
注意：以下只是参考输出，因为输入序列是随机的，每次输出结果并不固定
运行结果：
给定数值范围中的元素 [3, 2, 3, 4, 2, 3, 3, 2, 2, 2]
"""
if __name__ == '__main__':
    # # 1.初始化 multiprocessing.Pool()
    # pool = mp.Pool(mp.cpu_count())
    #
    # # 2.使用apply(), 将函数howmany_within_range作为主参传进去
    # results = [pool.apply(howmany_within_range, args=(row, 4, 8)) for row in data]
    #
    # # 3. 不要忘记关闭进程
    # pool.close()
    #
    # print("使用并行处理的：", results[:10])
    #
    #
    # def howmany_within_range_rowonly(row, minimum=4, maximum=8):
    #     count = 0
    #     for n in row:
    #         if minimum <= n <= maximum:
    #             count += 1
    #     return count
    #
    #
    # pool = mp.Pool(mp.cpu_count())
    # results = pool.map(howmany_within_range_rowonly, [row for row in data])
    # pool.close()
    # print(results[:10])

    import multiprocessing as mp

    pool = mp.Pool(mp.cpu_count())
    results = pool.starmap(howmany_within_range, [(row, 4, 8) for row in data])
    pool.close()
    print(results[:10])

