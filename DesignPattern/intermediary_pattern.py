# @Time    : 2020/10/17 10:10
# @Author  : GodWei
# @File    : intermediary_pattern.py
#  中介模式的框架模型

class InteractiveObject:
    """进行交涉的对象"""
    pass

class InteractiveObjectImplA:
    """实现类A"""
    pass

class InteractiveObjectImplB:
    """实现类B"""
    pass

class Meditor:
    """中介类"""

    def __int__(self):
        self.__interactiveObjA = InteractiveObjectImplA()
        self.__interactiveObjB = InteractiveObjectImplB()

    def interactive(self):
        """进行交互的操作"""
        # 通过 self.__interactiveObjA 和 self.__interactiveObjB完成相应的交互操作
        pass
