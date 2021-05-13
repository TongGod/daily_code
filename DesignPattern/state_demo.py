# @Time    : 2020/10/7 11:33
# @Author  : GodWei
# @File    : state_demo.py

# 引入 ABCMeta 和 abstractmethod 来定义抽象类和抽象方法
from abc import ABCMeta, abstractmethod


class Water:
    """水"""

    def __init__(self, state):
        self.__temperature = 25  # 默认常温为25℃
        self.__state = state

    def setState(self, state):
        self.__state = state

    def changeState(self, state):
        if self.__state:
            print("由", self.__state.getName(), "变为", state.getName())
        else:
            print("初始化为", state.getName())
        self.__state = state

    def getTemperature(self):
        return self.__temperature

    def setTemperature(self, temperature):
        self.__temperature = temperature
        if self.__temperature <= 0:
            self.changeState(SolidState("固态"))
        elif self.__temperature <= 100:
            self.changeState(LiquidState("液态"))
        else:
            self.changeState(GaseousState("气态"))

    def riseTemperature(self, step):
        self.setTemperature(self.__temperature + step)

    def reduceTemperature(self, step):
        self.setTemperature(self.__temperature - step)

    def behavior(self):
        self.__state.behavior(self)


class State(metaclass=ABCMeta):
    """状态的基类"""

    def __init__(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def isMatch(self, stateInfo):
        """状态的属性 stateInfo 是否在当前的状态范围"""
        return False

    @abstractmethod
    def behavior(self, water):
        """不同状态下的行为"""
        pass


class SolidState(State):
    """固态"""

    def __init__(self, name):
        super().__init__(name)

    def behavior(self, water):
        print("当前的温度" + str(water.getTemperature()) + "℃，为固态冰")


class LiquidState(State):
    """液态"""

    def __init__(self, name):
        super().__init__(name)

    def behavior(self, water):
        print("当前的温度" + str(water.getTemperature()) + "℃，为液态水")


class GaseousState(State):
    """气态"""

    def __init__(self, name):
        super().__init__(name)

    def behavior(self, water):
        print("当前的温度" + str(water.getTemperature()) + "℃，为气态水蒸气")


def testState():
    water = Water(LiquidState("液态"))
    water.behavior()
    water.setTemperature(-4)  # 设置温度
    water.behavior()
    water.riseTemperature(18)   # 提升温度18℃
    water.behavior()
    water.riseTemperature(110)  # 提升温度110℃
    water.behavior()

testState()
