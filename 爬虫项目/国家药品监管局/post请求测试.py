# @Time    : 2021/3/12 10:21
# @Author  : GodWei
# @File    : post请求测试.py
import requests

url = "http://app1.nmpa.gov.cn/data_nmpa/face3/search.jsp?6SQk6G2z=GBK-5SQBZKDU5OCZ_ar0T1M3thco8IJcRUqI1HXu_11Jt_jC71NVsDLZ60SuUFidsPtALHhWeHJCKsECaCAl1YlmjoqrKjUv1m1xEKdIL1YBAjAEsfSFNxSK9cWhz6994eq7Q7WgouBCG9T2ViD4B_oqfgpXkx6okVz7L_zDyrXG5TAQWZesMDyjM4u9oxqNDpANr8xpaJ.NzzDhTbdwa9bNpsA.Lzrk7_ME5TyOsi.dx4hkbP4NmJ5rD8qrwme8Iruqq.wHT6oJs2F2.L1aVKWiSrY8INXClaTSucOaC81rtQTN5Jg7JcTzqUrhJV2huaMIuvVIS4CSYWW4pmaSpdgHR1Dh9SOtEMpXMO9T2Hv_DS3E"
url1 = "http://app1.nmpa.gov.cn/data_nmpa/face3/base.jsp?tableId=21&tableName=TABLE21&title=%D2%BD%C1%C6%C6%F7%D0%B5%B1%EA%D7%BC%C4%BF%C2%BC&bcId=152904437880111023387499337007&CbSlDlH0=qAr5kqkPgXhPgXhPg2BsmZcaG8j_oNWnOQemHQAlhOEqqiE"
headers = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/70.0.3538.110 Mobile Safari/537.36 ",
    "Content-Type": "application/x-www-form-urlencoded",
    "Host": "app1.nmpa.gov.cn",
    "Accept": "*/*",
    "Referer": "http://app1.nmpa.gov.cn/data_nmpa/face3/base.jsp?tableId=21&tableName=TABLE21&title=%D2%BD%C1%C6%C6"
               "%F7%D0%B5%B1%EA%D7%BC%C4%BF%C2%BC&bcId=152904437880111023387499337007",
    "Cookie":"JSESSIONID=F625426EFE946456B37A7EDD72312B5A.7; neCYtZEjo8GmS=5CY1xuuLx.8o1J3fip.ToUbt.WE8Sa_vre9gCARbGnizPM7n.1NlLRlL0plLHzIZm9ut4DRK4KX4TiGTOOpghYa; acw_tc=276aedc316156003359961345e082791b2b29d5f4a9bd6300d600fdf155d8d; neCYtZEjo8GmT=53laFlKrWDNVqqqmgtYCR1GsxXajii4USlgbh9BYDbNoObDKDLhwkXrVN7SAFs.hbqrvuLkSdQeKGK5VTWsJzYGKb6Q6_R0h2n5woVMVbX2ZdM29UxCkKBvBwEIg9R_2E_3zodKVMzgMXEqtC4h6QUxXdGmN3lbnfyUiddRCzQ0emh7hzhAYrZiCMWXBDEzXAwdQvwCeqTFBZ1JEE25EVjUyiGbV28i0DwmvTg.SMENDEzyCiI.f3Uh9hm6E6IRfWmvIdryf2Hb9xc3gygrlTTKk0HJnpxgriz0rV9ZG9D89Z9UwCyn_aOn9ci.lA7dklE"
}
data = {
    "tableId": "137",
    "State": "1",
    "bcId": "154209525480914914535208988760",
    "curstart": "4",
    "tableName": "TABLE137",
    "viewtitleName": "COLUMN1853",
    "viewsubTitleName": "COLUMN1854",
    "tableView": "%E5%8C%BB%E7%96%97%E5%99%A8%E6%A2%B0%E7%BB%8F%E8%90%A5%E4%BC%81%E4%B8%9A%EF%BC%88%E5%A4%87%E6%A1%88%EF%BC%89",
    "cid": "0",
    "ytableId": "0",
    "searchType": "search"
}
requests.session()
r = requests.post(url=url, headers=headers, data=data)
print(r.text)
