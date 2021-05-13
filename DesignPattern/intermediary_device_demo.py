# @Time    : 2020/10/18 19:51
# @Author  : GodWei
# @File    : intermediary_device_demo.py

# 基于框架的实现
from abc import ABCMeta, abstractmethod
# 引入 ABCMeta 和 abstractmethod 来定义抽象类和抽象方法
from enum import Enum


class DeviceMgr(metaclass=ABCMeta):

    @abstractmethod
    def enumerate(self):
        """枚举设备列表（在程序初始化时，有设备插拔时都要重新获取设备列表）"""
        pass

    @abstractmethod
    def active(self, deviceId):
        """选择要使用的设备"""
        pass

    @abstractmethod
    def getCurDeviceId(self):
        """获取当前正在使用的设备"""
        pass


class DeviceType(Enum):
    """设备类型"""
    TypeSpeaker = 1
    TypeMicrophone = 2
    TypeCamera = 3


class DeviceList:
    """设备列表"""

    def __init__(self):
        self.__devices = []

    def add(self, deviceItem):
        self.__devices.append(deviceItem)

    def getCount(self):
        return len(self.__devices)

    def getByIdx(self, idx):
        if idx < 0 or idx >= self.getCount():
            return None
        return self.__devices[idx]

    def getById(self, id):
        for item in self.__devices:
            if item.getId() == id:
                return item
        return None


class DeviceItem:
    """设备项"""

    def __init__(self, id, name, type, isDefault=False):
        self.__id = id
        self.__name = name
        self.__type = type
        self.__isDefault = isDefault

    def __str__(self):
        return "type:" + str(self.__type) + "\nid:" + str(self.__id) \
               + "\nname：" + str(self.__name) + "\nisDefault:" + str(self.__isDefault) + "\n"

    def getId(self):
        return self.__id

    def getName(self):
        return self.__name

    def getType(self):
        return self.__type

    def isDefault(self):
        return self.__isDefault


class SpeakerMgr(DeviceMgr):
    """扬声器设备管理类"""

    def __init__(self):
        self.__curDeviceId = None

    def enumerate(self):
        """枚举设备列表
         （真实的项目应该通过驱动程序去读取设备信息，这里只用初始化来模拟）
        """
        devices = DeviceList()
        devices.add(DeviceItem("HDAUDIO\FUNC_01&VEN_10EC&DEV_0235&SUBSYS_104315E0&REV_1000",
                               "Realtek High Definition Audio", DeviceType.TypeSpeaker))
        devices.add(DeviceItem("HDAUDIO\FUNC_02&VEN_20EC&DEV_0258&SUBSYS_267459E0&REV_2000",
                               "Realtek High Definition Audio", DeviceType.TypeSpeaker, True))
        return devices

    def active(self, deviceId):
        """激活指定的设备作为当前要用的设备"""
        self.__curDeviceId = deviceId

    def getCurDeviceId(self):
        return self.__curDeviceId


class DeviceUtil:
    """设备工具类"""

    def __init__(self):
        self.__mgrs = {}
        self.__mgrs[DeviceType.TypeSpeaker] = SpeakerMgr()
        # 作为演示，MicrophoneMgr 和 CameraMgr 不再实现
        # self.__microphoneMgr = MicrophoneMgr()
        # self.__cameraMgr = CameraMgr()

    def __getDeviceMgr(self, type):
        return self.__mgrs[type]

    def getDeviceList(self, type):
        return self.__getDeviceMgr(type).enumerate()

    def active(self, type, deviceId):
        self.__getDeviceMgr(type).active(deviceId)

    def getCurDeviceId(self, type):
        return self.__getDeviceMgr(type).getCurDeviceId()


def testDevices():
    deviceUtil = DeviceUtil()

    deviceList = deviceUtil.getDeviceList(DeviceType.TypeSpeaker)

    print("麦克风设备列表：")
    if deviceList.getCount() > 0:
        # 设置第一个设备为要用的设备
        deviceUtil.active(DeviceType.TypeSpeaker, deviceList.getByIdx(0).getId())
    for idx in range(0, deviceList.getCount()):
        device = deviceList.getByIdx(idx)
        print(device)
    print(deviceList.getById(deviceUtil.getCurDeviceId(DeviceType.TypeSpeaker)))


testDevices()
