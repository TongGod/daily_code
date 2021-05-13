import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

df = pd.read_csv("./bank.csv")
# 1.     6:4分割
traindata_df = df.head(int(len(df) * 0.6) + 1)  # 前面60%
testdata_df = df.tail(int(len(df) * 0.4))  # 剩下的40%
traindata_df.to_csv("./TrainData.csv", header=True, index=False)
print("TrainData.csv文件保存成功")
testdata_df.to_csv("./TestData.csv", header=True, index=False)
print("TestData.csv文件保存成功")

#  （二）1..TrainData.csv文件去空和去重复
traindata_df.dropna(axis=0, how='any')
traindata_df.drop_duplicates(keep='first', inplace=False)
# （二）2.最大值和最小值和中位数
max_value = traindata_df['age'].max()
print('*'*30)
print("最大值为:", max_value)
min_value = traindata_df['age'].min()
print('*'*30)
print("最小值为:", min_value)
median_value = int(traindata_df['age'].median())
print('*'*30)
print("中位数为:", median_value)
# （二）3.分组
groupby_df = traindata_df.groupby('education', axis=0)['nr_employed'].mean()
print('*'*30)
print("分组后的平均值：")
print(groupby_df)

# (三) 画图
plt.figure(figsize=(12, 9))
# 1.直方图
axes1 = plt.subplot(1, 2, 1)
data_bar = dict(zip(*np.unique(list(df["age"]), return_counts=True)))
bar_x = list(data_bar.keys())
bar_y = list(data_bar.values())
axes1.bar(bar_x, bar_y)
axes1.set_title("age直方图")
axes1.set_xticks(list(range(0, len(bar_x) + 5, 5)))

# 2.曲线图
axes2 = plt.subplot(1, 2, 2)
axes2.plot(bar_x, bar_y)
axes2.set_title("age曲线图")
axes2.set_xticks(list(range(0, len(bar_x) + 5, 5)))
# plt.show()
plt.savefig("./age.png")
print('*'*30)
print("age.png已保存")
