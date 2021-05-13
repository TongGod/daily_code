import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("mysql+pymysql://root:123456@localhost/douban?charset=utf8")

df = pd.read_csv('./data.csv')

df['id'] = list(range(1, len(df) + 1))
df.to_sql(name='douban_game', con=engine, if_exists='append', index=False, index_label=False)
print("数据保存成功！！！")
