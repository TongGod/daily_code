# @Time    : 2021/3/5 8:28
# @Author  : GodWei
# @File    : 01.py
from selenium import webdriver


browser = webdriver.Chrome()
browser.get('http://app1.nmpa.gov.cn/data_nmpa/face3/base.jsp?tableId=21&tableName=TABLE21&title=%D2%BD%C1%C6%C6%F7%D0%B5%B1%EA%D7%BC%C4%BF%C2%BC&bcId=152904437880111023387499337007')
print(browser.get_cookies())


