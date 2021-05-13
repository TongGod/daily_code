import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


class Draw:
    def __init__(self):
        plt.rcParams['font.sans-serif'] = ['SimHei']  # 解决中文乱码
        self.df = pd.read_csv('./data.csv', encoding='gbk')

    # 岗位分析
    def job_analysis(self):
        title_count = dict(zip(*np.unique(list(self.df['title']), return_counts=True)))
        title_dict = {'job_name': list(title_count.keys()), 'count': list(title_count.values())}
        df_title_dict = pd.DataFrame(title_dict)
        df_title = df_title_dict.sort_values(by="count", ascending=False)
        df_top = df_title.head(10)  # 取出前10名

        # 对前10名以后的数据进行处理
        other_job = int(df_title['count'][9:].sum())
        # 画图所需的数据
        df_top_name = list(df_top['job_name'])
        for i in range(0, len(df_top_name)):
            if 4 < len(df_top_name[i]) < 9:
                df_top_name[i] = df_top_name[i][:3] + "\n" + df_top_name[i][3:]

            elif len(df_top_name[i]) > 8:
                df_top_name[i] = df_top_name[i][:6] + "\n" + df_top_name[i][6:]

        df_top_count = list(df_top['count'])
        plt.figure(figsize=(13, 10))
        axes1 = plt.subplot(1, 2, 1)
        # 两张图之间的间隔
        plt.subplots_adjust(wspace=0.3)
        explode = (0.1, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        axes1.pie(df_top_count, labels=df_top_name, autopct='%1.1f%%', shadow=True, explode=explode)
        axes1.set_title('岗位分析饼状图', size=15)
        axes2 = plt.subplot(1, 2, 2)
        axes2.bar(range(0, 20, 2), df_top_count)
        axes2.set_title('岗位分析柱状图', size=15)
        # 给柱状图添加数据标签
        for a, b in zip(range(0, 20, 2), df_top_count):
            axes2.text(a, b + 0.05, '%.0f' % b, ha='center', va='bottom', fontsize=10)
        plt.xticks(range(0, 20, 2), df_top_name, rotation=70)
        axes2.set_ylabel('岗位数量', position=(0, 1), rotation=0)
        plt.savefig('./img/岗位分析.png')
        plt.close()
        print("岗位分析成功，分析结果已保存！！！")

    # 行业分析
    def job_industry(self):
        occ_count = dict(zip(*np.unique(list(self.df['company_ind']), return_counts=True)))
        occ_dict = {'occ_name': list(occ_count.keys()), 'count': list(occ_count.values())}
        df_occ_dict = pd.DataFrame(occ_dict)
        df_occ = df_occ_dict.sort_values(by="count", ascending=False)
        df_top = df_occ.head(10)  # 取出前10名
        explode = (0.1, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        plt.pie(list(df_top['count']), labels=list(df_top['occ_name']), autopct='%1.1f%%', shadow=True, explode=explode)
        plt.title("行业分析", size=15)
        plt.savefig('./img/行业分析.png')
        plt.close()
        print("行业分析成功，分析结果已保存！！！")

    # 经验要求
    def job_ex(self):
        ex_count = dict(zip(*np.unique(list(self.df['experience']), return_counts=True)))
        explode = (0.1, 0, 0, 0.1, 0, 0, 0)
        plt.pie(list(ex_count.values())[:-1], labels=list(ex_count.keys())[:-1], autopct='%1.1f%%', shadow=True,
                explode=explode)
        plt.title("经验要求", size=15)
        plt.savefig('./img/经验要求.png')
        plt.close()
        print("经验要求分析成功，分析结果已保存！！！")

    # 学历要求
    def job_edu(self):
        edu_count = dict(zip(*np.unique(list(self.df['education']), return_counts=True)))
        edu_count.pop('暂无')
        edu_name = ['博士', '硕士', '本科', '大专', '中专', '中技', '高中', '初中及以下']
        edu_name = edu_name[::-1]
        count_list = []
        for i in edu_name:
            count_list.append(edu_count[i])
        plt.barh(range(0, 8), count_list)
        plt.title("学历要求", size=15)
        plt.xticks(range(0, 7000, 500))
        plt.text(6800, -1, "数量")
        plt.text(-450, 7.9, "学历")
        plt.yticks(range(0, 8), edu_name)
        for a, b in zip(range(0, 8), count_list):
            plt.text(b + 50, a - 0.15, '%.0f' % b, fontsize=10)
        plt.savefig('./img/学历要求.png')
        plt.close()
        print("学历要求分析成功，分析结果已保存！！！")

    # 薪资分析
    def salary_analysis(self):
        # 设置画布
        plt.figure(figsize=(19.2, 10.8))

        # 最大薪资分布情况
        max_wage_count = dict(zip(*np.unique(list(self.df['max_wage']), return_counts=True)))
        max_wage_x = list(max_wage_count.keys())[:-3][1:]
        max_wage_y = list(max_wage_count.values())[:-3][1:]
        axes = plt.subplot(2, 2, 1)
        axes.set_title("最大薪酬分布情况", loc='left')
        axes.set_xlabel("每月薪酬（单位：万/月）")
        axes.set_ylabel("职位数量")
        axes.bar(max_wage_x, max_wage_y, color='orange')

        # 城市薪酬分析图
        axes2 = plt.subplot(2, 2, 2)
        df = self.df.sort_values(by='max_wage')
        area_x = list(df['area'])
        area_y = list(df['max_wage'])
        city_x, city_y = [], []
        for i in range(0, len(area_x)):
            if area_x[i] != "异地招聘":
                city_x.append(area_x[i])
                city_y.append(area_y[i])
        city_x = city_x[:-3][1:][::-1][:15]
        for i in range(0, len(city_x)):
            if "-" in city_x[i]:
                city_x[i] = "\n".join(city_x[i].split("-"))
        city_y = city_y[:-3][1:][::-1][:15]
        axes2.bar(city_x, city_y, color='purple')
        axes2.set_title("城市薪酬分析图", loc='left')
        axes2.set_xlabel("城市地区")
        axes2.set_ylabel("每月薪酬（单位：万/月）")

        # 工作经验平均薪酬分析图
        grouped = self.df.groupby(by='experience')
        ex_grouped = grouped.mean()
        ex_name = ex_grouped._stat_axis.values.tolist()
        axes3 = plt.subplot(2, 2, 3)
        axes3.set_title("工作经验平均薪酬", loc='left')
        axes3.set_xlabel("工作经验要求")
        axes3.set_ylabel("每月薪酬（单位：万/月）")
        axes3.bar([i - 0.2 for i in range(len(ex_name))], list(ex_grouped['min_wage']), color='#0000E3', label="最小薪酬",
                  width=0.3)
        axes3.bar([i + 0.1 for i in range(len(ex_name))], list(ex_grouped['avg_wage']), color='#007979', label="平均薪酬",
                  width=0.3)
        axes3.bar([i + 0.4 for i in range(len(ex_name))], list(ex_grouped['max_wage']), color='#00BB00', label="最大薪酬",
                  width=0.3)
        axes3.set_xticks([i + 0.1 for i in range(len(ex_name))])
        axes3.set_xticklabels(ex_name)
        axes3.legend()

        # 平均薪酬最高的前10名岗位
        df = self.df.sort_values(by='avg_wage')
        df = df[df['title'].str.contains('大数据|算法|智能|AI|工程师|架构师|开发|Python|python|分析|Java|java|Hadoop|运维|JAVA|后台|全栈|PHP'
                                         '|数据')]
        job_name = list(df['title'])[:-3][::-1][:10]
        for i in range(0, len(job_name)):
            if len(job_name[i]) >= 8:
                job_name[i] = job_name[i][:8] + "\n" + job_name[i][8:]
        top_job = list(df['max_wage'])[:-3][::-1][:10]
        axes4 = plt.subplot(2, 2, 4)
        axes4.set_title("薪酬最高的前10名岗位", loc='left')
        axes4.set_xlabel("每月薪酬（单位：万/月）")
        axes4.set_ylabel("岗位名称")
        axes4.barh(job_name, top_job, color='#007979')
        plt.subplots_adjust(hspace=0.35, wspace=0.3)
        plt.savefig('./img/薪资分析.png')
        plt.close()
        print("薪资分析成功，分析结果已保存！！！")


if __name__ == '__main__':
    draw = Draw()
    # 岗位分析图
    draw.job_analysis()
    # 行业分析图
    draw.job_industry()
    # 经验要求图
    draw.job_ex()
    # 学历要求
    draw.job_edu()
    # 薪资分析
    draw.salary_analysis()
    print("---------所有的图已经绘制完毕！-------")
