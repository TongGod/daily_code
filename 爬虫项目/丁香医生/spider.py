import requests
import json
import xlwt
import os
import time

# url字段
url_city = 'https://ask.dxy.com/view/i/sectiongroup/member/modules?dxa_adplatform=m.dxy.com&all_city=1'
url_doctoer_base = 'https://ask.dxy.com/view/i/sectiongroup/member?dxa_adplatform=m.dxy.com&page_index={}&items_per_page=100&section_group_id={}&id={}&ad_status=0&limit_price=true&tertiary_hospital=false&rank_type=0&area_type={}'
url_profile_base = 'https://ask.dxy.com/view/i/doctor/profile?doctor_user_id={}&volunteer_care=false&referral=false'
url_group = 'https://ask.dxy.com/view/i/sectiongroup/list?dxa_adplatform=m.dxy.com&page_index=1&items_per_page=200&append=true&key=sectionList'

f = open('err.txt', 'w', encoding='utf-8')

# 变量数据
areas = []  # 城市信息
groups = []  # 科室信息

errCount = 0
errlist = ''
grpIndex = 1  # 科室查询到哪一步了

saveFileName = 'DATA'
rowCount = 1
# 创建一个workbook 设置编码
workbook = xlwt.Workbook(encoding='utf-8')
# 创建一个worksheet
worksheet = workbook.add_sheet('My Worksheet')


# 初始化excel


def InitExcel():
    global worksheet
    worksheet.write(0, 0, label='姓名')
    worksheet.write(0, 1, label='省')
    worksheet.write(0, 2, label='市')
    worksheet.write(0, 3, label='查询科室')
    worksheet.write(0, 4, label='医生科室')
    worksheet.write(0, 5, label='职位')
    worksheet.write(0, 6, label='工作单位')
    worksheet.write(0, 7, label='简介')
    worksheet.write(0, 8, label='评分')
    worksheet.write(0, 9, label='响应时间')
    worksheet.write(0, 10, label='月回答数')
    worksheet.write(0, 11, label='处方数')
    worksheet.write(0, 12, label='一级标签')
    worksheet.write(0, 13, label='二级擅长')
    worksheet.write(0, 14, label='图文价格')
    worksheet.write(0, 15, label='电话价格')
    worksheet.write(0, 16, label='医生卡')
    worksheet.write(0, 17, label='二级标签')
    worksheet.write(0, 18, label='一级擅长')
    worksheet.write(0, 19, label='医院等级')


# 获取城市信息
def GetAreas():
    headers = {
        'Host': 'ask.dxy.com',
        'user-agent': 'Mozilla/5.0'
    }
    jsonStr = requests.get(url_city, headers=headers).text
    global areas
    areas = json.loads(jsonStr)


# 获取科室


def GetGroups():
    headers = {
        'Host': 'ask.dxy.com',
        'user-agent': 'Mozilla/5.0'
    }
    jsonStr = requests.get(url_group, headers=headers).text
    global groups
    groups = json.loads(jsonStr)


# 获取医生列表


def GetDoctoers(groupid, group, cityid, province, city, index):
    global errCount
    # 获取医师列表
    headers = {
        'Host': 'ask.dxy.com',
        'user-agent': 'Mozilla/5.0'
    }
    jsonDots = None
    global grpIndex
    global groups
    global errList
    global errCount
    url = url_doctoer_base.format(index, groupid, groupid, cityid)
    jsonStr = requests.get(url, headers=headers).text
    try:
        jsonDots = json.loads(jsonStr)
    except Exception as err:
        GetDoctoers(groupid, group, cityid, province, city, index)

    grpLen = len(groups['data']['items'])
    # 获取医师详细信息
    for doct in jsonDots['data']['items']:
        try:
            detial = GetDoctoer(doct['id'])
            os.system('cls')
            print('当前完成进度(总)[{}/{}]'.format(grpIndex, grpLen))
            print('失败数:{}'.format(errCount))
            # print('当前科室地区的进度[{}/{}]')
            print('[{}] : [{}]科,[{}]省,[{}]市,[{}])'.format(rowCount, group, province, city, doct['doctor']['nickname']))
            WriteData(doct=doct, detial=detial, province=province, city=city, group=group)
            workbook.save(saveFileName + '.xls')
        except Exception as err:
            errCount += 1
            errList += doct['id'] + '\n'
            f.write(contents)
        time.sleep(1)

    if index < jsonDots['data']['total_pages']:
        index += 1
        GetDoctoers(groupid, group, cityid, province, city, index)

    # 获取医生详细信息


def GetDoctoer(id):
    url_profile = url_profile_base.format(id)
    # payload = {}
    headers = {
        'Host': 'ask.dxy.com',
        'user-agent': 'Mozilla/5.0'
    }
    response = requests.request("GET", url_profile, headers=headers)
    return json.loads(response.text)


# 保存数据
def WriteData(doct, detial, province, city, group):
    global rowCount
    global worksheet
    worksheet.write(rowCount, 0, label=doct['doctor']['nickname'])
    worksheet.write(rowCount, 1, label=province)
    worksheet.write(rowCount, 2, label=city)
    worksheet.write(rowCount, 3, label=group)
    worksheet.write(rowCount, 4, label=doct['doctor']['section_name'])
    worksheet.write(rowCount, 5, label=doct['doctor']['job_title_name'])
    worksheet.write(rowCount, 6, label=doct['doctor']['hospital_name'])
    worksheet.write(rowCount, 7, label=doct['doctor']['self_desc'])
    worksheet.write(rowCount, 8, label=doct['doctor']['average_star'])
    worksheet.write(rowCount, 9, label=doct['doctor']['avg_reply_time_v2_str'])
    worksheet.write(rowCount, 10, label=doct['doctor']['reply_count'])
    worksheet.write(rowCount, 11, label=doct['doctor']['prescription_count'])

    # 这个是一级标签
    tagStr = ''
    for tag in doct['doctor']['list_operate_tags']:
        tagStr = tagStr + tag['name'] + ','
    worksheet.write(rowCount, 12, label=tagStr)

    # 这个是擅长方向
    tagStr = ''
    for data in detial['data']['items'][0]['hot_counsel_list_v2']:
        tagStr += '{}({}),'.format(data['tag_name'], data['question_count'])
    worksheet.write(rowCount, 13, label=tagStr)
    worksheet.write(rowCount, 14, label=doct['doctor']['setting_price'])
    worksheet.write(rowCount, 15, label=doct['doctor']['make_call_price'])

    # 医生卡
    cardStr = ''
    if 'vip_card_recommend' in detial['data']['items'][0]:
        cardInfo = detial['data']['items'][0]['vip_card_recommend']
        cardStr = '{},{}'.format(cardInfo['title'], cardInfo['content'])
    worksheet.write(rowCount, 16, cardStr)

    # 二级标签
    tagStr = ''
    for data in detial['data']['items'][0]['doctor']['marking_tags']:
        tagStr += '{},'.format(data['name'])
    worksheet.write(rowCount, 17, label=tagStr)

    # 一级擅长
    tagStr = '擅长'
    for tag in doct['doctor']['tags']:
        tagStr += '{}、'.format(tag)
    worksheet.write(rowCount, 18, label=tagStr)

    # 三甲
    if 'hospital_info' in doct['doctor']:
        if doct['doctor']['hospital_info']['tertiary_hospital'] == True:
            worksheet.write(rowCount, 19, label='三甲')
        else:
            worksheet.write(rowCount, 19, label='')
    else:
        worksheet.write(rowCount, 19, label='')

    rowCount += 1


def main():
    InitExcel()
    GetAreas()
    # print(areas)
    GetGroups()
    global grpIndex
    for grp in groups['data']['items']:
        for prov in areas['data']['items'][1]['list_modules']:
            if prov['text'] == '热门城市':
                continue

            for cit in prov['children']:
                if cit['text'] == prov['text']:
                    continue

                groupid = grp['id']
                group = grp['name']
                cityid = cit['value']
                city = cit['text']
                province = prov['text']
                index = 1
                GetDoctoers(groupid, group, cityid, province, city, index)

        grpIndex += 1
    print('下载完成')
    x = input()


if __name__ == '__main__':
    main()

# 14
