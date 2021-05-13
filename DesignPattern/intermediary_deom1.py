# @Time    : 2020/10/17 10:17
# @Author  : GodWei
# @File    : intermediary_deom1.py


class HousingAgency:
    """房屋中介"""

    def __init__(self, name):
        self.__houseInfos = []
        self.__name = name

    def getName(self):
        return self.__name

    # 添加房源信息
    def addHouseInfo(self, houseInfo):
        if houseInfo not in self.__houseInfos:
            self.__houseInfos.append(houseInfo)

    # 删除房源信息
    def removeHouseInfo(self, houseInfo):
        for info in self.__houseInfos:
            if info == houseInfo:
                self.__houseInfos.remove(info)

    # 搜索客户需求的房源信息
    def getSearchCondition(self, description):
        """这里有一个将用户描述信息转换成搜索条件的逻辑（这里只是简单的演示，就原样进行描述）"""
        return description

    def getMatchInfos(self, searchCondition):
        """根据房源信息（这里只进行演示，所以省略去匹配的过程，全部输出）"""
        print(self.getName(), "为您找到以下最合适的房源：")
        for info in self.__houseInfos:
            info.showInfo(False)
        return self.__houseInfos

    def signContract(self, houseInfo, period):
        """与房东签订协议"""
        print(self.getName(), "与房东", houseInfo.getOwnerName(), "签订", houseInfo.getAddress(),
              "的房子的租赁合同，租期", period, "年。 合同期内", self.getName(), "有权对其进行使用和转租！")

    def signContracts(self, period):
        for info in self.__houseInfos:
            self.signContract(info, period)


class HouseInfo:
    """房源信息"""

    def __init__(self, address, area, price, hasWindow, hasBathroom, kitchen, owner):
        self.__area = area
        self.__price = price
        self.__address = address
        self.__hasWindow = hasWindow
        self.__kitchen = kitchen
        self.__hasBathroom = hasBathroom
        self.__owner = owner

    def getAddress(self):
        return self.__address

    def getOwnerName(self):
        return self.__owner.getName()

    def showInfo(self, isShowOwner=True):
        print(
            "面积:" + str(self.__area) + "平方米",
            "价格:" + str(self.__price) + "元",
            "窗户:" + ("有" if self.__hasWindow else "没有"),
            "卫生间:" + self.__hasBathroom,
            "厨房:" + ("有" if self.__hasWindow else "没有"),
            "地址:" + self.__address,
            "房东:" + self.getOwnerName() if isShowOwner else ""
        )


class HouseOwner:
    """房东"""

    def __init__(self, name):
        self.__name = name
        self.__houseInfo = None

    def getName(self):
        return self.__name

    def setHouseInfo(self, address, area, price, hasWindow, bathroom, kitchen):
        self.__houseInfo = HouseInfo(address, area, price, hasWindow, bathroom, kitchen, self)

    # 推送房源信息
    def publishHouseInfo(self, agency):
        agency.addHouseInfo(self.__houseInfo)
        print(self.getName() + "在", agency.getName(), "发布房源出租信息：")
        self.__houseInfo.showInfo()


class Customer:
    """用户"""

    def __init__(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def findHouse(self, description, agency):
        print("我是" + self.getName() + "，我想要找一个\"" + description + "\"的房子")
        print()
        return agency.getMatchInfos(agency.getSearchCondition(description))

    def seeHouse(self, houseInfos):
        """去看房，去看最实用的房子，制作演示，省略过程"""
        size = len(houseInfos)
        return houseInfos[size - 1]

    def signContract(self, houseInfo, agency, period):
        """与中介签订协议"""
        print(self.getName(), "与中介", agency.getName(), "签订", houseInfo.getAddress(),
              "的房子的租赁合同，租期", period, "年。合同期内", self.__name, "有权利其进行使用！")


def testRenting():
    # 中介名称
    myHome = HousingAgency("我爱我家")
    # 房主信息
    zhangsan = HouseOwner("张三")
    # 设置房主的出租信息
    zhangsan.setHouseInfo("上地西里", 20, 2500, 1, "独立卫生间", 0)
    # 房主把出租的信息推送给中介
    zhangsan.publishHouseInfo(myHome)

    lisi = HouseOwner("李四")
    lisi.setHouseInfo("当代城市家园", 16, 1800, 1, "公共卫生间", 0)
    lisi.publishHouseInfo(myHome)

    wangwu = HouseOwner("王五")
    wangwu.setHouseInfo("金隅美和园", 18, 2600, 1, "独立卫生间", 1)
    wangwu.publishHouseInfo(myHome)

    print()

    # 中介房东签合同，3年期限
    myHome.signContracts(3)
    print()

    tony = Customer("Tong")
    houseInfos = tony.findHouse("18平方米左右，要有独立卫生间，要有窗户，最好朝南，有厨房更好！价位在2000元左右", myHome)
    print()
    print("正在看房")
    print()
    AppropriateHouse = tony.seeHouse(houseInfos)
    tony.signContract(AppropriateHouse, myHome, 1)


testRenting()
