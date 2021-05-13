# @Time    : 2020/9/28 17:48
# @Author  : GodWei
# @File    : enumerationMethod.py
#  枚举算法

# 24点游戏
import itertools


# 计算24点游戏代码
def twentyfour(cards):
    """
        (1)itertools.permutations(可迭代对象)：
            通俗地讲，就是返回可迭代对象的所有数学全排列方式。
            itertools.permutations("1118") -> 即将数字1118进行全排列组合
        (2)itertools.product(*iterables, repeat=1)
            iterables是可迭代对象,repeat指定iterable重复几次
            返回一个或者多个iterables中的元素的笛卡尔积的元组
            即为product(list1, list2) 依次取出list1中的每1个元素，与list2中的每1个元素，组成元组，
            repeat即为元组中有几个元素，最多重复几次
        (3)
    """
    for num in itertools.permutations(cards):
        for ops in itertools.product("+-*/", repeat=3):
            # ({0}{4}{1}){5}({2}{6}{3}) - > 即在{0}{1}{2}{3}放上数字，{4}{5}{6}放上运算符号，只能放三个，四个数字中间只能放三个运算符
            # 带括号有8种方法
            # 1. (ab)cd
            bsd1 = '({0}{4}{1}){5}{2}{6}{3}'.format(*num, *ops)
            # 2. a(bc)d
            bsd2 = '{0}{4}({1}{5}{2}){6}{3}'.format(*num, *ops)
            # 3. ab(cd)
            bsd3 = '{0}{4}{1}{5}({2}{6}{3})'.format(*num, *ops)
            # 4. (ab)(cd)
            bsd4 = '({0}{4}{1}){5}({2}{6}{3})'.format(*num, *ops)
            # 5. ((ab)c)d
            bsd5 = '(({0}{4}{1}){5}{2}){6}{3}'.format(*num, *ops)
            # 6.  (a(bc))d
            bsd6 = '({0}{4}({1}{5}{2})){6}{3}'.format(*num, *ops)
            # 7.  a((bc)d)
            bsd7 = '{0}{4}(({1}{5}{2}){6}{3})'.format(*num, *ops)
            # 8.  a(b(cd))
            bsd8 = '{0}{4}({1}{5}({2}{6}{3}))'.format(*num, *ops)
            # print([bsd1, bsd2, bsd3, bsd4, bsd5, bsd6, bsd7, bsd8])
            for bds in [bsd1, bsd2, bsd3, bsd4, bsd5, bsd6, bsd7, bsd8]:
                try:
                    if abs(eval(bds) - 24.0) < 1e-20:
                        return "24点结果 = "+bds
                except ZeroDivisionError:  # 零除错误
                    continue
    return "Not fond"

cards = ['2484', '1126', '1127', '1128', '2484', '1111']
for card in cards:
    print(twentyfour(card))
