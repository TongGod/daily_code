# @Time    : 2020/9/27 11:56
# @Author  : GodWei
# @File    : observerPattern.py

from abc import ABCMeta, abstractmethod, ABC


# 引入ABCMeta 和 abstractmethod 来定义抽象类和抽象方法

# metaclass=ABCMeta ： 使创建的类为抽象类
class Observer(metaclass=ABCMeta):
    """观察者的基类"""

    @abstractmethod
    def update(self, observable, object):
        pass


class Observable:
    """被观察者的基类"""

    def __init__(self):
        self.__observers = []

    # 添加观察者
    def addObserver(self, observer):
        self.__observers.append(observer)

    # 删除观察者
    def removeObserver(self, observer):
        self.__observers.remove(observer)

    # 内容或状态变化时通知所有的观察者
    def notifyObservers(self, object=0):
        for o in self.__observers:
            o.update(self, object)


class WasterHeater(Observable):
    """热水器的类，继承父类（被观察者的抽象类）"""

    def __init__(self):
        super().__init__()
        self.__temperature = 25

    def getTemperature(self):
        return self.__temperature

    def setTemperature(self, temperature):
        self.__temperature = temperature
        print("当前的温度是", str(temperature), "℃")
        self.notifyObservers()


class WashingMode(Observer):
    """洗澡的类，继承父类（观察者的抽象类）"""

    def update(self, observable, object):
        if isinstance(observable, WasterHeater) \
                and 50 <= observable.getTemperature() <= 70:
            print("水已经烧好，可以洗澡")


class DrinkingMode(Observer):
    """喝水的类，继承父类（观察者的抽象类）"""

    def update(self, observable, object):
        if isinstance(observable, WasterHeater) \
                and  observable.getTemperature() >= 100:
            print("水已经烧开，可以饮用")

def testWaterHeatper():
    heater = WasterHeater()  # 创建热水器类的对象
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