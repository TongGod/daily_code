import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("mysql+pymysql://root:123456@localhost/novel_rank?charset=utf8")


def save_mysql(path, table_name):
    df = pd.read_csv(path)
    df.insert(0, 'id', list(range(1, len(df) + 1)))
    df.to_sql(name=table_name, con=engine, if_exists='append', index=False, index_label=False)
    print("{}数据保存到{}成功！！！".format(path, table_name))


save_mysql('./hengyan_data.csv', 'hengyan')
save_mysql('./zongheng_data.csv', 'zongheng')
save_mysql('./chuangshi_data.csv', 'chuangshi')
