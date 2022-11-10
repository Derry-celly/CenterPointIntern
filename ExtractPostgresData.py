# 1: 读配置文件：
#   数据库连接
#   查询列
#   行数
#   查询条件

# 2: 连数据库，查询数据

# 3: 将数据导出到csv
#import ConfigFile


hostname = "localhost"
database = "insurance"
username = "postgres"
port_id = "5432"
pwd = "100910"

import psycopg2
import csv
import pandas as pd

try:
    conn = psycopg2.connect(
    dbname = database,
    user =username,
    password = pwd,
    host = hostname,
    port = port_id)

    cursor = conn.cursor()
    postgres_select_query = "select * from ads_dws.hmb_ads_dws_ads_dws_dm_hmb_column"
    cursor.execute(postgres_select_query)
    print("Selecting rows from ads_dws.hmb_ads_dws_ads_dws_dm_hmb_column table using cursor.fetchall")
    hmb_ads_dws_ads_dws_dm_hmb_column_records = cursor.fetchall()


except Exception as error:
    print(error)

'''sql_query = pd.read_sql_query(postgres_select_query, conn, )
df = pd.DataFrame(sql_query)
df.to_csv(r'/Users/derrickchen/Documents/圆心科技/Example.csv', index = False)
print("Finished!")'''

conn.closed()




