import pandas as pd
import glob
import datetime

data_path = glob.glob('./*.csv')
print(data_path)
df = pd.DataFrame()
for path in data_path:
    df_select = pd.read_csv(path)
    print(df_select.head())
    #df_select.drop(columns=['Uname:0'], inplace=True)
    df = pd.concat([df, df_select])

df.info()
print(df.head())
print(df.category.value_counts())
df.to_csv('./news_titles_{}'.format(datetime.datetime.now().strftime("%Y%m%d")), index=False)
