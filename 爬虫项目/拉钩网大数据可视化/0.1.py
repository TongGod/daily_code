from bs4 import BeautifulSoup
import re
import urllib.request,urllib.error
import xlwt
import sqlite3
def main():
    baseurl = "https://movie.douban.com/top250?start="
   #1.爬取网页
    datalist = getData(baseurl)
    savepath = "豆瓣电影Top250.xls"
   #3.保存数据
    saveData(datalist,savepath)
    #askURL("https://movie.douban.com/top250?start=")


findlink = re.compile(r'<a href="(.*?)">')#影片详情链接
findImgSrc = re.compile(r'<img.*src="(.*?)"',re.S)#让换行符包含在字符中 #影片图片链接
findtitle = re.compile(r'<span class="title">(.*)</span>')#影片片名
findRating = re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')#影片评分
findJudge = re.compile(r'<span>(\d*)人评价</span>')
findInq = re.compile(r'<span class="inq">(.*)</span>')
findBd = re.compile(r'<p class="">(.*?)</p>',re.S)

#爬取网页
def getData(baseurl):
    datalist = []
    for i in range(0,10):
        url =baseurl + str(i*25)
        html = askURL(url)
        #2.逐一解析
        soup = BeautifulSoup(html,"html.parser")
        for item in soup.find_all('div',class_="item"):
            #print(item)#测试查看电影item全部信息。
            data=[]
            item = str(item)

            link = re.findall(findlink,item)[0]
            data.append(link)
            imgSrc = re.findall(findImgSrc,item)[0]
            data.append(imgSrc)
            titles = re.findall(findtitle,item)
            if(len(titles)==2):
                ctitle = titles[0]
                data.append(ctitle)
                otitle = titles[1].replace("/","")
                data.append(otitle)
            else:
                data.append(titles[0])
                data.append('')
            reting =re.findall(findRating,item)[0]
            data.append(reting)

            judgeNum = re.findall(findJudge,item)[0]
            data.append(judgeNum)

            inq = re.findall(findInq,item)
            if(len(inq)!=0):
                inq = inq[0].replace("。","")
                data.append(inq)
            else:
                data.append("")
            bd = re.findall(findBd,item)[0]
            bd = re.sub('<br(\s+)?/>(\s+)?'," ",bd)
            bd = re.sub('/'," ",bd)
            data.append(bd.strip())

            datalist.append(data)
    print(datalist)
    return datalist
#得到指定网站url内容
def askURL(url):
    head = {
        "User-Agent":"Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 84.0.4147.89Safari / 537.36"
    }
    request = urllib.request.Request(url,headers=head)
    html = ""
    try:
        response = urllib.request.urlopen(request)
        html= response.read().decode("utf-8")
        #print(html)

    except urllib.error.URLError as e:
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)
    return html






#保存网页数据
def saveData(datalist,savepath):
    book = xlwt.Workbook(encoding="utf-8",style_compression=0)
    sheet = book.add_sheet('豆瓣电影TOP250',cell_overwrite_ok=True)
    col = ("电影详情链接","图片链接","影片中文名","影片外国名","评分","评分数","概况","相关信息")
    for i in range(0,8):
        sheet.write(0,i,col[i])
    for i in range(0,250):
        print("第%d条"%(i+1))
        data = datalist[i]
        for j in range(0,8):
            sheet.write(i+1,j,data[j])

    book.save(savepath)






if __name__== "__main__":
    main()