# @Time    : 2021/4/6 17:41
# @Author  : GodWei
# @File    : 快速排序.py

def quick_sort(arr):
    """快速排序"""
    if len(arr) < 2:
        return arr
    # 选取基准，随便选哪个都可以，选中间的便于理解
    mid = arr[len(arr) // 2]
    # 定义基准值左右两个数列
    left, right = [], []
    # 从原始数组中移除基准值
    arr.remove(mid)
    for item in arr:
        # 大于基准值放右边
        if item >= mid:
            right.append(item)
        else:
            # 小于基准值放左边
            left.append(item)
    return quick_sort(left) + [mid] + quick_sort(right)


if __name__ == '__main__':
    a = [11, 99, 33, 69, 77, 88, 55, 11, 33, 36, 39, 66, 44, 22]
    print(a)
    print(quick_sort(a))
