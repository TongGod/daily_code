# @Time    : 2021/3/12 16:07
# @Author  : GodWei
# @File    : 自动化获取cookie.py

from selenium import webdriver



# 不开网页搜索
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')

driver = webdriver.Chrome(options=chrome_options)

driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
    "source": """
    Object.defineProperty(navigator, 'webdriver', {
      get: () => undefined
    })
  """
})
driver.get("http://app1.nmpa.gov.cn/data_nmpa/face3/base.jsp?tableId=21&tableName=TABLE21&title=%D2%BD%C1%C6%C6%F7%D0%B5%B1%EA%D7%BC%C4%BF%C2%BC&bcId=152904437880111023387499337007")
print(driver.get_cookie(name="JSESSIONID"))

# cookie = [item["name"] + "=" + item["value"] for item in driver.get_cookies()]
# # join()连接字符串数组。将字符串、元组、列表中的元素以指定的字符(分隔符)连接生成一个新的字符串
# cookiestr = ';'.join(item for item in cookie)
#
# # 保存处理过的cookie
# with open("cookie.txt", 'wb') as f:
#     f.write(cookiestr)
# print("cookie保存成功")