# @Time    : 2020/10/14 20:31
# @Author  : GodWei
# @File    : Divide_Conquer_query_min.py

# 划分（基于主元 pivot）
def partition(seq):
    pi = seq[0]  # 挑选主元
    min_pi = [x for x in seq[1:] if x <= pi]  # 所有小于主元的元素
    max_pi = [x for x in seq[1:] if x > pi]  # 所有大于主元的元素
    return pi, min_pi, max_pi


# 查找第 K 小的元素
def select(seq, k):
    # 分解
    pi, min_pi, max_pi = partition(seq)
    min_pi_length = len(min_pi)  # 所有小于主元的元素长度
    # 如果查第 k 小的元素刚好和 比主元小的元素列表长度 相等，则此时pi(主元)则刚好为第K小的元素
    if min_pi_length == k:
        return pi
    # 长度小于k时，
    elif min_pi_length < k:
        # 分治、递归
        return select(max_pi, k - min_pi_length - 1)
    else:
        # 分治、递归
        return select(min_pi, k)


if __name__ == '__main__':
    seq = [12, 6, 5956, 7, 8, 98, 46, 46, 4, 451, 9684, 4]
    print(seq)
    print("列表中第3小的：", select(seq, 3))
    print("列表中第1小的：", select(seq, 1))
