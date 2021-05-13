from selenium import webdriver


# 获取cookie
def get_cookies():
    chrome_options = webdriver.ChromeOptions()

    driver = webdriver.Chrome(options=chrome_options)

    # driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
    #     "source": """
    #     Object.defineProperty(navigator, 'webdriver', {
    #       get: () => undefined
    #     })
    #   """
    # })
    driver.get("https://www.lagou.com/")
    for i in driver.get_cookies():
        print(i)
    #print(driver.get_cookies())
    # 进行cookie的拼接
    # cookies_dic = {
    #     "JSESSIONID": driver.get_cookie("JSESSIONID")["value"],
    #     "WEBTJ-ID": driver.get_cookie("WEBTJ-ID")["value"],
    #     "user_trace_token": driver.get_cookie("user_trace_token")["value"],
    #     "LGUID": driver.get_cookie("LGUID")["value"],
    #     "_ga": driver.get_cookie("_ga")["value"],
    #     "_gid": driver.get_cookie("_gid")["value"],
    #     "index_location_city": "%E5%85%A8%E5%9B%BD",
    #     "__lg_stoken__": "4cf05d1f4f3dfda3ed5280e46fea64ef21eddc1e1e4871646793a47e0905a8e515049ab213546726a140de84e1b884e8d61d9254a19d799ffae29d5ed814930d6077e032f55e",
    #     "X_MIDDLE_TOKEN": "ef6f1e7dba29f2358e96502363802085",
    #     "TG-TRACK-CODE": "index_search",
    #     "SEARCH_ID": "a5fdae06e7bc42a4b425dabf8f6344c4",
    #     "LGSID": driver.get_cookie("LGSID")["value"],
    #     "PRE_UTM": driver.get_cookie("PRE_UTM")["value"],
    #     "PRE_HOST": driver.get_cookie("PRE_HOST")["value"],
    #     "PRE_SITE": driver.get_cookie("PRE_SITE")["value"],
    #     "PRE_LAND": driver.get_cookie("PRE_LAND")["value"],
    #     "sensorsdata2015jssdkcross": driver.get_cookie("sensorsdata2015jssdkcross")["value"],
    #     "Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6": driver.get_cookie("Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6")[
    #         "value"],
    #     "LGRID": driver.get_cookie("LGRID")["value"]
    # }
    #
    # cookie = ""
    # for i in range(0, len(list(cookies_dic.keys()))):
    #     cookie = cookie + list(cookies_dic.keys())[i] + "=" + str(list(cookies_dic.values())[i]) + ";"
    # print(cookie)
get_cookies()