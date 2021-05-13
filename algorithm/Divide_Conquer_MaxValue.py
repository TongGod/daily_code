# @Time    : 2020/10/14 16:44
# @Author  : GodWei
# @File    : Divide_Conquer_MaxValue.py

# 基本子算法（子问题规模小于或等于2时）
def get_max(max_list):
    return max(max_list)


# 分治法
def solve(init_list):
    list_length = len(init_list)
    # 若问题规模小于或等于2时，直接调用方法解决完成
    if list_length <= 2:
        return get_max(init_list)

    # 问题规模大时，开始分治算法的步骤
    # 1.分解（子问题的规模为   n/2）,分别取列表其中的前半部分和后半部分
    left_list = init_list[:list_length // 2]
    right_list = init_list[list_length // 2:]

    # 2.分治、递归(一直递归，分解，知道求出前半部分的最大值，和后半部分的最大值)
    left_max = solve(left_list)
    right_max = solve(right_list)

    # 3.合并 （在把前半部分的最大值和后半部分的最大值做个比较，相当于求整个大数组的最大值）
    return get_max([left_max, right_max])


if __name__ == '__main__':
    test_list = [12, 6, 5956, 7, 8, 98, 46, 46, 4, 451, 9684, 4]
    # 打印出最大值
    print(solve(test_list))
    # 9684