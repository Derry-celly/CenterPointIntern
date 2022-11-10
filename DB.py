import pandas as pd
import psycopg2
import pandas

hostname = 'localhost'
database = 'insurance'
username = 'postgres'
port_id = '5432'
pwd = '100910'

conn = psycopg2.connect(
    dbname = database,
    user = username,
    password = pwd,
    host = hostname,
    port = port_id

)
cursor = conn.cursor()
query1 = "select insurance_id, insured_amount, pay_amount, insured_total_amount, pay_status, insurance_product_code from ads_dws.hmb_insurance_core_yueyang_pro_if_user_insure"
cursor.execute(query1)
#print(cursor.fetchall())

query = pd.read_sql_query(query1, conn)
df = pd.DataFrame(query)
df.to_csv(r'/Users/derrickchen/Documents/圆心科技/project_2/file_1', index = False)


query2 = "select insurance_id, insured_fee_amount, pay_amount, insured_total_amount, pay_status, insurance_product_code from ads_dws.hmb_ads_dws_ads_dws_policy_tbl1_drs_tmp where insurance_product_code = 'YUEYANG2021001'"
cursor.execute(query2)
queryy = pd.read_sql_query(query2, conn)
df = pd.DataFrame(queryy)
df.to_csv(r'/Users/derrickchen/Documents/圆心科技/project_2/file_2', index = False)
print("Finished!")