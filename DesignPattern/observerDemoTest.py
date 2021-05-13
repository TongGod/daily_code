# @Time    : 2020/9/27 11:56
# @Author  : GodWei
# @File    : observerPattern.py

from abc import ABCMeta, abstractmethod


# 热水器类
class WaterHeater:

    def __init__(self):
        # 观察者的数量
        self.__observers = []
        # 设置初始温度
        self.__temperature = 25

    # 获取温度
    def getTemperature(self):
        return self.__temperature

    # 设置温度
    def setTemperature(self, temperature):
        self.__temperature = temperature
        print("当前的温度是", str(temperature), "℃")
        # 调用notifies方法，其实就是调用每个观察者中的update
        self.notifies()

    def addObserver(self, observer):
        self.__observers.append(observer)

    def notifies(self):
        for o in self.__observers:
            o.update(self, )


# 创建观察者的抽象类
class Observer(metaclass=ABCMeta):
    """观察者的基类"""

    @abstractmethod
    def update(self, observalbe, object):
        pass


# 洗澡的类WashingMode继承父类Observer
class WashingMode(Observer):

    # 重写父类中静态方法update
    def update(self, waterHeater, **kwargs):
        if 50 <= waterHeater.getTemperature() <= 70:
            print("水已经烧好，可以洗澡")


# 喝水的类DrinkingMode继承父类Observer
class DrinkingMode(Observer):

    # 重写父类中静态方法update
    def update(self, waterHeater, **kwargs):
        if waterHeater.getTemperature() >= 100:
            print("水已经烧开，可以饮用了")


def testWaterHeatper():
    heater = WaterHeater()  # 创建热水器类的对象
    washingObser = WashingMode()  # 创建洗澡类的对象
    drinkingObser = DrinkingMode()  # 创建喝水类的对象
    # 调用热水器对象的添加观察者(洗澡类对象)的方法
    heater.addObserver(washingObser)
    # 调用热水器对象的添加观察者(喝水类对象)的方法
    heater.addObserver(drinkingObser)
    # 设置各种温度
    heater.setTemperature(40)
    heater.setTemperature(60)
    heater.setTemperature(100)

# 调用测试方法
testWaterHeatper()
