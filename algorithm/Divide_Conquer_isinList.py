# @Time    : 2020/10/14 19:02
# @Author  : GodWei
# @File    : Divide_Conquer_isinList.py

# 子问题算法（子问题规模为1）
def is_in_list(init_list, el):
    return [False, True][init_list[0] == el]


# 分治法
def solve(init_list, el):
    list_length = len(init_list)
    if list_length == 1:  # 若问题规模等于1，即列表中
        return is_in_list(init_list, el)

    # 分解（子问题规模为 n/2）
    left_list = init_list[:list_length // 2]
    right_list = init_list[list_length // 2:]

    # 分治合并  递归（一直进行拆分，   or 只有所有都是 False，才返回假 False）
    # 所以只要有一个元素在里面，就判定元素在该列表中，
    res = solve(left_list, el) or solve(right_list, el)

    return res


if __name__ == '__main__':
    test_list = [12, 6, 5956, 7, 8, 98, 46, 46, 4, 451, 9684, 4]
    # 查找
    print(test_list)
    print("判断45是否在列表中:", solve(test_list, 45))
    print("判断4是否在列表中:", solve(test_list, 4))
