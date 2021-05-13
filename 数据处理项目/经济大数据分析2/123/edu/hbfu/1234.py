import pandas as pd


def csv_file(df):
    df = df.dropna()
    df.to_csv("./TrainData.csv", index=False, header=True)
    print("TrainData.csv文件保存成功！")


def data_handle():
    df = pd.read_csv("./TrainData.csv")
    print("age列的最大值:", df["age"].max())
    print("age列的最小值:", df["age"].min())
    print("age列的最中位值:", df["age"].median())


if __name__ == '__main__':
    df = pd.read_csv("./cs-training.csv")
    # 去除空值,存入TrainData.csv
    csv_file(df)
    # 读取TrainData.csv，打印age列中的最大值，最小值和中位数
    data_handle()
