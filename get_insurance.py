import psycopg2
from read_config import read_config
import pandas as pd
from read_business import read_business



def get_insurance():
    conn = None
    try:
        params = read_config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute('Select * from ads_dws.hmb_ads_dws_ads_dws_dm_hmb_column', conn)

        print('The number of rows:', cur.rowcount)
        row = cur.fetchone()
        num = 0
        for row in cur.fetchone():
            num += 1
        print(num)

        fileindex = 1
        index = 0

        '''while row is not None:
             if index < numbers:
                 fileindex += 1
                 print(row)
                 row = cur.fetchone()'''





    except(Exception, psycopg2.DatabaseError) as error:
        print(error)



    finally:
        sql_query = pd.read_sql_query('Select * from ads_dws.hmb_ads_dws_ads_dws_dm_hmb_column', conn,)
        df = pd.DataFrame(sql_query)
        df.to_csv(r'/Users/derrickchen/Documents/圆心科技/example.csv', index=False)
        cur.close()
        if conn is not None:
            conn.close()





if __name__ == '__main__':
    get_insurance()

