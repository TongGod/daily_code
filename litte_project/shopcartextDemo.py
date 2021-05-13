# @Time    : 2020/8/31 10:44
# @Author  : GodWei
# @File    : shopcartextDemo.py
"""
思路：
    1.引导用户输入金额
    2.引导用户选择商品
    3.根据用户的选择将商品添加到购物车
    4.删除商品
    5.结算购物车，退出系统
"""

# 购物车
# 商品名称作为key,商品数量作为value
shoppingcar = {}


# 添加商品
def addgoods(product, num):
    if num.isdigit():  # isdigit()如果字符串只包含数字则返回 True 否则返回 False。
        num = int(num)
        # 判断key是否存在
        if product not in shoppingcar:
            # 添加键值对
            shoppingcar[product] = num
        else:
            # 修改指定键的值
            shoppingcar[product] += num
        print("商品添加成功")
    else:
        print("数量输入有误")


def delgoods(name, num):
    product = 0
    for key in shoppingcar:
        if key[0] == name:
            product = key
    if num.isdigit():
        num = int(num)
        if num >= shoppingcar[product]:
            for product in shoppingcar:
                if product[0] == name:
                    # 删除该商品的全部
                    shoppingcar.pop(product)
        else:
            # 删除该商品指定的数量【修改value值】
            shoppingcar[product] -= num

        print("商品删除成功")
    else:
        print("数量输入有误")


if __name__ == '__main__':
    print("**********==========欢迎进入自选超市==========**********")
    # 引导用户输入金额
    saving = input("请输入你的金额：")

    if saving.isdigit():
        saving = int(saving)
        while True:
            print("可以进行的操作如下：\n "
                  "0.添加商品  1.删除商品  2.结算购物车  3.退出超市")
            # 引导用户选择操作
            choice = input("请输入你需要进行的操作：")

            if choice in ["0", "1", "2", "3"]:
                if choice == '0':
                    # 添加
                    # 存储商品的列表
                    product_list = [
                        ('book', 88),
                        ('iphone', 8888),
                        ('food', 100),
                        ('kindle', 500),
                        ('computer', 7000)
                    ]
                    # 展示商品内容
                    print("本商店的商品如下：")
                    for i, goods in enumerate(product_list):
                        print("%d:%s" % (i, goods))

                    # 引导用户选择商品
                    index = input("请输入你需要购买的商品编号：")

                    if index.isdigit():
                        index = int(index)
                        if 0 <= index <= len(product_list) - 1:
                            # 获取商品
                            product = product_list[index]

                            # 引导用户输入商品数量
                            num = input("请输入需要购买的%s的数量：" % (product[0]))

                            if int(num) * product[1] > saving:
                                print("金额不足，请充值")
                                saving += int(input("请输入需要充值的金额："))
                                print("充值成功，余额为：%d" % saving)
                            else:
                                # 减去商品价格
                                saving -= int(num) * product[1]
                                # 将商品添加到购物车
                                addgoods(product, num)
                    else:
                        print("商品的编号输入有误")
                elif choice == '1':
                    # 删除
                    name = input("请输入需要删除的商品名称：")
                    num = input("请输入需要删除的商品的数量：")
                    for product in shoppingcar:
                        if product[0] == name:
                            # 添加金额
                            saving += int(num) * product[1]
                    delgoods(name, num)
                elif choice == '2':
                    # 结算购物车
                    print("----------你已经购买了如下商品----------")
                    for key,value in shoppingcar.items():
                        print("%s:%s"%(key,value))

                    # 清空购物车
                    shoppingcar.clear()
                    print("你还剩余%d元" % saving)

                else:
                    # 退出
                    print("欢迎再次光临")
                    break
            else:
                print("暂未开通此功能")
    else:
        print("金额输入有误，请重新输入")
