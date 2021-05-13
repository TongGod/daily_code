# @Time    : 2020/10/8 21:56
# @Author  : GodWei
# @File    : state_use_Demo.py

# 引入 ABCMeta 和 abstractmethod 来定义抽象类和抽象方法
from abc import ABCMeta, abstractmethod


class Context(metaclass=ABCMeta):
    """状态模式的上下文环境类"""

    def __init__(self):
        self.__states = []
        self.__curState = None
        self.__stateInfo = None
        # 状态发生变化依赖的属性，当这一变量由多个变量共同决定时可以将其单独定义成一个类
        self._stateInfo = 0

    def addState(self, state):
        if state not in self.__states:
            self.__states.append(state)

    def changeState(self, state):
        if state is None:
            return False
        if self.__curState is None:
            print("初始化为", state.getName())
        else:
            print("由", self.__curState.getName(), "变为", state.getName())
        self.__curState = state
        self.addState(state)
        return True

    def getState(self):
        return self.__curState

    def setStateInfo(self, stateInfo):
        self.__stateInfo = stateInfo
        for state in self.__states:
            if state.isMatch(stateInfo):
                self.changeState(state)

    def getStateInfo(self):
        return self.__stateInfo


class Water(Context):
    """水"""

    def __init__(self):
        super().__init__()
        # 添加三种状态
        self.addState(SolidState("固态"))
        self.addState(LiquidState("液态"))
        self.addState(GaseousState("气态"))
        # 设置温度
        self.setTemperature(25)

    def getTemperature(self):
        return self.getStateInfo()

    def setTemperature(self, temperature):
        self.setStateInfo(temperature)

    def riseTemperature(self, step):
        self.setTemperature(self.getTemperature() + step)

    def reduceTemperature(self, step):
        self.setTemperature(self.getTemperature() - step)

    def behavior(self):
        # 获取状态
        state = self.getState()
        if isinstance(state, State):
            state.behavior(self)


# 单例的装饰器
def singleton(cls, *args, **kwargs):
    """构造一个单例的装饰器"""
    instance = {}

    def _singleton(*args, **kwargs):
        if cls not in instance:
            instance[cls] = cls(*args, **kwargs)
        return instance[cls]

    return _singleton


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


@singleton
class SolidState(State):
    """固态"""

    def __init__(self, name):
        super().__init__(name)

    def isMatch(self, stateInfo):
        return stateInfo < 0

    def behavior(self, context):
        print("当前的温度" + str(context.getStateInfo()) + "℃，为固态冰")


class LiquidState(State):
    """液态"""

    def __init__(self, name):
        super().__init__(name)

    def isMatch(self, stateInfo):
        return 0 <= stateInfo < 100

    def behavior(self, context):
        print("当前的温度" + str(context.getStateInfo()) + "℃，为液态水")


class GaseousState(State):
    """气态"""

    def __init__(self, name):
        super().__init__(name)

    # 当温度大于100，即为气态，范围true
    def isMatch(self, stateInfo):
        return stateInfo >= 100

    def behavior(self, context):
        print("当前的温度" + str(context.getStateInfo()) + "℃，为气态水蒸气")


def testState():
    water = Water()
    water.behavior()
    water.setTemperature(-4)  # 设置温度
    water.behavior()
    water.riseTemperature(18)  # 提升温度18℃
    water.behavior()
    water.riseTemperature(110)  # 提升温度110℃
    water.behavior()


testState()

