import re
import pandas as pd


# 薪资的处理
def salary_process(df):
    min_wage_list, max_wage_list, avg_wage_list = [], [], []
    salary_info = list(df['provide_salary'])  # 取出未清洗的薪资那一列
    # 对异常的工资进行处理
    for i in range(0, len(salary_info)):
        # 处理空值，有空值的全部添加为0
        if type(salary_info[i]) == float:
            min_wage_list.append(0)
            max_wage_list.append(0)
            avg_wage_list.append(0)
        # 处理元/小时，处理时候，减去周六周日的时间，
        # 最高按照一个月(31天-8(四个周六周日))，最低按照一个月(28天-8(四个周六周日))
        # 平均去最高最低的平均  （下面的元/天，同理）
        elif str(salary_info[i])[-1] == "时":
            number_max = round((float(re.findall('(.*?)元.*?', salary_info[i], re.S)[0]) * 24 * (31 - 8)) / 10000, 1)
            number_min = round((float(re.findall('(.*?)元.*?', salary_info[i], re.S)[0]) * 24 * (28 - 8)) / 10000, 1)
            number_avg = round((number_max + number_min) / 2, 1)
            min_wage_list.append(number_min)
            max_wage_list.append(number_max)
            avg_wage_list.append(number_avg)
        # 处理元/天（与上同理）
        elif str(salary_info[i])[-1] == "天":
            number_max = round((float(re.findall('(.*?)元.*?', salary_info[i], re.S)[0]) * (31 - 8)) / 10000, 1)
            number_min = round((float(re.findall('(.*?)元.*?', salary_info[i], re.S)[0]) * (28 - 8)) / 10000, 1)
            number_avg = round((number_max + number_min) / 2, 1)
            min_wage_list.append(number_min)
            max_wage_list.append(number_max)
            avg_wage_list.append(number_avg)
        # 处理 万/年
        elif str(salary_info[i])[-3:] == "万/年":
            min_wage = round(float(re.findall('(.*?)-.*?', salary_info[i], re.S)[0]) / 12, 1)
            max_wage = round(float(re.findall('.*?-(.*?)万', salary_info[i], re.S)[0]) / 12, 1)
            avg_wage = round((min_wage + max_wage) / 2, 1)  # 保留一位小数
            min_wage_list.append(min_wage)
            max_wage_list.append(max_wage)
            avg_wage_list.append(avg_wage)
        # 处理 千/月
        elif str(salary_info[i])[-3:] == "千/月":
            min_wage = round(float(re.findall('(.*?)-.*?', salary_info[i], re.S)[0]) / 10, 1)
            max_wage = round(float(re.findall('.*?-(.*?)千', salary_info[i], re.S)[0]) / 10, 1)
            avg_wage = round((min_wage + max_wage) / 2, 1)  # 保留一位小数
            min_wage_list.append(min_wage)
            max_wage_list.append(max_wage)
            avg_wage_list.append(avg_wage)
        # 其他的情况最大取最大，最小取最大的一半
        elif '以上/年' in str(salary_info[i]) or '以下/年' in str(salary_info[i]):
            number = float(re.findall('(.*?)万', salary_info[i], re.S)[0])
            max_wage = round(number / 12, 1)
            min_wage = round((number / 2) / 12, 1)
            avg_wage = round((min_wage + max_wage) / 2, 1)  # 保留一位小数
            min_wage_list.append(min_wage)
            max_wage_list.append(max_wage)
            avg_wage_list.append(avg_wage)
        elif '以下/月' in str(salary_info[i]):
            number = float(re.findall('(.*?)千', salary_info[i], re.S)[0])
            max_wage = round(number / 10, 1)
            min_wage = round((number / 2) / 10, 1)
            avg_wage = round((min_wage + max_wage) / 2, 1)  # 保留一位小数
            min_wage_list.append(min_wage)
            max_wage_list.append(max_wage)
            avg_wage_list.append(avg_wage)
        # 即为正常的值 万/月
        else:
            min_wage = round(float(re.findall('(.*?)-.*?', salary_info[i], re.S)[0]), 1)
            max_wage = round(float(re.findall('.*?-(.*?)万', salary_info[i], re.S)[0]), 1)
            avg_wage = round((min_wage + max_wage) / 2, 1)  # 保留一位小数
            min_wage_list.append(min_wage)
            max_wage_list.append(max_wage)
            avg_wage_list.append(avg_wage)
    df["min_wage"] = min_wage_list
    df["max_wage"] = max_wage_list
    df['avg_wage'] = avg_wage_list
    return df


# 处理缺乏工作经验以及学历的要求列表中的空缺，缺失添加为暂无
def null_process(df):
    attribute_list = list(df['attribute'])  # 取出df中attribute的数据，转化为列表
    for i in range(0, len(attribute_list)):
        if "经验" not in attribute_list[i]:
            attribute = eval(attribute_list[i])
            attribute.insert(1, "暂无")
            attribute_list[i] = str(attribute)
        flag = True
        for edu in ["本科", "硕士", "大专", "博士", "高中", "中技", "中专", "初中及以下"]:
            if edu in attribute_list[i]:
                flag = False
        if flag:
            attribute = eval(attribute_list[i])
            attribute.insert(2, "暂无")
            attribute_list[i] = str(attribute)
    df['attribute'] = attribute_list
    return df


# 拆分最后一列的合成列表,处理attribute的列表的值
def split_info(df):
    area = []
    experience = []
    education = []
    number = []
    attribute_list = list(df["attribute"])
    for i in range(0, len(attribute_list)):
        area.append(eval(attribute_list[i])[0])
        experience.append(eval(attribute_list[i])[1])
        education.append(eval(attribute_list[i])[2])
        number.append(eval(attribute_list[i])[3])
    df['area'] = area
    df['experience'] = experience
    df['education'] = education
    df['number'] = number
    df = df.drop(labels="attribute", axis=1)
    df.reset_index(drop=True, inplace=True) # 重新设置行索引
    return df


if __name__ == '__main__':
    CSV_FILE_PATH = './unprocess_data.csv'  # 读取路径
    df = pd.read_csv(CSV_FILE_PATH)  # 读取文件
    # 处理公司规模的空值
    df['company_size'].fillna('暂无', inplace=True)
    # 处理attribute中的缺失值
    df = null_process(df)
    # 分隔attribute列表，合成新的DataFrame
    df = split_info(df)
    # 薪资的处理
    df = salary_process(df)
    df['provide_salary'].fillna(0, inplace=True)  # 填充工资中的空值
    # 处理公司类型的空值
    df['company_type'].fillna('暂无', inplace=True)
    # 将数据进行保存
    df.to_csv("./data.csv", header=True, index=False, encoding="gbk")
    print("数据处理并保存成功！！！")
