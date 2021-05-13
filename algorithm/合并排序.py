# @Time    : 2021/4/6 16:35
# @Author  : GodWei
# @File    : 合并排序.py

import random


def merge_sort(str):
    # 如果只有一个元素，则返回列表值
    if len(str) <= 1:
        return str
    # 取列表中间的位置
    mid = int(len(str) / 2)
    # 递归地排序其左边和右边的子列表
    left = merge_sort(str[:mid])
    right = merge_sort(str[mid:len(str)])
    result = []  # 最后排好序的列表

    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))

    if len(left) > 0:
        result.extend(merge_sort(left))
        print(result)
    else:
        result.extend(merge_sort(right))
    return result


if __name__ == '__main__':
    a = [20, 30, 64, 16, 8, 0, 99, 24, 75, 100, 69]
    print(a)
    print(merge_sort(a))
    # b = [random.randint(1, 1000) for i in range(10)]
    # print(merge_sort(b))
