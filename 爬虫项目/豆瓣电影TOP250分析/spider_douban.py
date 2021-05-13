import time

from bs4 import BeautifulSoup
import re
import urllib.request, urllib.error
import xlwt


def main():
    baseurl = "https://movie.douban.com/top250?start="
    # 1.爬取网页
    datalist = getData(baseurl)
    savepath = "douban_Top250.xls"
    # 3.保存数据
    saveData(datalist, savepath)


findlink = re.compile(r'<a href="(.*?)">')  # 影片详情链接
findImgSrc = re.compile(r'<img.*src="(.*?)"', re.S)  # 让换行符包含在字符中 #影片图片链接
findtitle = re.compile(r'<span class="title">(.*)</span>')  # 影片片名
findRating = re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')  # 影片评分
findJudge = re.compile(r'<span>(\d*)人评价</span>')
findInq = re.compile(r'<span class="inq">(.*)</span>')
findBd = re.compile(r'<p class="">(.*?)</p>', re.S)


# 爬取网页
def getData(baseurl):
    datalist = []
    for i in range(0, 10):
        url = baseurl + str(i * 25)
        html = askURL(url)
        # 2.逐一解析
        soup = BeautifulSoup(html, "html.parser")
        for item in soup.find_all('div', class_="item"):
            # print(item)#测试查看电影item全部信息。
            data = []
            item = str(item)

            link = re.findall(findlink, item)[0]
            data.append(link)
            imgSrc = re.findall(findImgSrc, item)[0]
            data.append(imgSrc)
            titles = re.findall(findtitle, item)
            if (len(titles) == 2):
                ctitle = titles[0]
                data.append(ctitle)
                otitle = titles[1].replace("/", "")
                data.append(otitle)
            else:
                data.append(titles[0])
                data.append('')
            reting = re.findall(findRating, item)[0]
            data.append(reting)

            judgeNum = re.findall(findJudge, item)[0]
            data.append(judgeNum)

            inq = re.findall(findInq, item)
            if (len(inq) != 0):
                inq = inq[0].replace("。", "")
                data.append(inq)
            else:
                data.append("")

            bd = re.findall(findBd, item)[0]

            bd = re.sub('<br(\s+)?/>(\s+)?', " ", bd)
            data.append(bd.strip())

            datalist.append(data)
    return datalist


# 得到指定网站url内容
def askURL(url):
    head = {
        "User-Agent": "Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 84.0.4147.89Safari / 537.36",
        "Cookie": 'll="118371"; bid=SlK45q_AUdw; __yadk_uid=UX8Da1Bda1ll6LVuo88F5rqIVkyrZXzh; __gads=ID=6139d3921f3415fb-22b0568ac4c600b1:T=1616481904:RT=1616481904:S=ALNI_MbfW0QCttA4LAQUucijYf7mvNiVTQ; __utmc=30149280; __utmz=223695111.1616901090.2.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmc=223695111; ap_v=0,6.0; dbcl2="184672824:EIBw0o1PpeY"; ck=9Es2; push_doumail_num=0; __utmt=1; __utmv=30149280.18467; __utmt_douban=1; __utma=223695111.1854253431.1616481747.1616999933.1617002968.4; __utmb=223695111.0.10.1617002968; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1617002968%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DB6PUSCL_bdyAoWDWTSHjlZR2lfKCJRZsmFQCf5vWcsss90DKCXAz67lGtElJNzxP%26wd%3D%26eqid%3Dabbdc1c600055c1d00000002605ff3de%22%5D; _pk_ses.100001.4cf6=*; __utma=30149280.994300030.1616422494.1617002944.1617002982.7; __utmz=30149280.1617002982.7.5.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; push_noty_num=0; __utmb=30149280.2.10.1617002982; _pk_id.100001.4cf6=00a98ae373ca10d7.1616481747.4.1617003033.1617001041.'
    }
    request = urllib.request.Request(url, headers=head)

    html = ""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")

    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)
    return html


# 保存网页数据
def saveData(datalist, savepath):
    global data_info
    book = xlwt.Workbook(encoding="utf-8", style_compression=0)
    sheet = book.add_sheet('douban_TOP250', cell_overwrite_ok=True)
    col = (
        "movie_url", "img_url", "name_chinese", "name_out", "score", "score_num", "survey", "year", 'country', 'type',
        "top")
    for i in range(0, 11):
        sheet.write(0, i, col[i])
    for i in range(0, 250):
        print("第%d条" % (i + 1))
        data = datalist[i]
        data_info = data[-1].split("...")[-1].split("/")
        for k in range(0, len(data_info)):
            data_info[k] = " ".join(data_info[k].split())
        if i == 18:
            data_info = ['2002', '中国香港', '剧情 犯罪 悬疑']
        if i == 29:
            data_info = ['1994', '中国大陆 中国香港', '剧情 历史 家庭']
        if i == 32:
            data_info = ['2001', '美国 英国', '奇幻 冒险']
        if i == 49:
            data_info = ['2004', '中国大陆', '动画 奇幻']
        if i == 63:
            data_info = ['1998', '英国', '剧情 喜剧 犯罪']
        if i == 104:
            data_info = ['1994', '中国大陆 中国香港', '剧情 爱情']
        if i == 134:
            data_info = ['1983', '中国大陆', '动画 奇幻']
        if i == 179:
            data_info = ['1988', '日本', '动画 剧情 战争']
        if i == 192:
            data_info = ['2006', '中国大陆 中国香港', '喜剧 犯罪']
        if i == 198:
            data_info = ['2015', '中国大陆', '纪录片']
        if i == 234:
            data_info = ['2003', '中国香港', '动作 犯罪 剧情 惊悚']
        data = data[:-1] + data_info
        data.append(i + 1)
        for j in range(0, 11):
            sheet.write(i + 1, j, data[j])

    book.save(savepath)


if __name__ == "__main__":
    main()
