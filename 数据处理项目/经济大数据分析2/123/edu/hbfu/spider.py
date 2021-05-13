import requests
from lxml import etree
import pandas as pd

get_url = "https://www.hbfu.edu.cn/"

r = requests.get(url=get_url)
text = r.text
html = etree.HTML(text)
new_info = html.xpath("//ul[@id='xyxwList']//li//a//text()")
new_date = html.xpath("//ul[@id='xyxwList']//li//span//text()")
dic = {
    "new_info": new_info,
    "new_date": new_date
}
df = pd.DataFrame(dic)
df.to_csv("./list.csv", index=False, header=True)
print("list.csv文件保存成功！")
