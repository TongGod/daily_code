# @Time    : 2020/9/28 11:10
# @Author  : GodWei
# @File    : login_observer.py
import time
from abc import ABCMeta, abstractmethod


# 使用监听模式的框架
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


class Account(Observable):
    """用户账户"""

    def __init__(self):
        super().__init__()
        self.__latestIp = {}
        self.__latestRegion = {}

    def login(self, name, ip, time):
        region = self.__getRegion(ip)
        if self.__isLongDistance(name, region):
            self.notifyObservers({"name": name, "ip": ip, "region": region, "time": time})
        self.__latestRegion[name] = region
        self.__latestIp[name] = ip

    def __getRegion(self, ip):
        """由Ip地址获取地区信息，（只是进行模拟）"""
        ipRegions = {
            "117.23.33.34": "陕西省咸阳市",
            "66.117.31.255": "美国洛杉矶"

        }
        region = ipRegions.get(ip)
        if region is None:
            return ""
        else:
            return region

    def __isLongDistance(self, name, region):
        """计算本次登录与最近登录的地区差距(只是简单的进行模拟，用字符串匹配模拟) """
        latestRegion = self.__latestRegion.get(name)
        if latestRegion is not None and latestRegion != region:
            return latestRegion


class SmsSender(Observer):
    """短信发送器"""

    def update(self, observable, object):
        print("【短信发送】" + object["name"] + "您好！系统检测到您的账户可能登录异常。最近一次登录信息：\n"
              + "  登录地区：" + object["region"] + "  登录ip :" + object["ip"] +
              "  登录时间：" + time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(object["time"])))


class MailSender(Observer):
    """邮件发送器"""

    def update(self, observable, object):
        print("【邮件发送】" + object["name"] + "您好！系统检测到您的账户可能登录异常。最近一次登录信息：\n"
              + "  登录地区：" + object["region"] + "  登录ip :" + object["ip"] +
              "  登录时间：" + time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(object["time"])))


def testLogin():
    accout = Account()
    accout.addObserver(SmsSender())
    accout.addObserver(MailSender())
    accout.login("GodWei ", "117.23.33.34", time.time())
    accout.login("GodWei ", "66.117.31.255", time.time())


testLogin()
