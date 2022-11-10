from configparser import ConfigParser

import psycopg2
from read_config import read_config

# 使用psycopg2库，和数据库建立连接。

def connect():
    conn = None
    try:
        params = read_config()
        print("Connecting to the PostgreSQL database...")
        conn = psycopg2.connect(**params)

        cur = conn.cursor()
        print('PostgreSQL database version:')
        cur.execute('SELECT version()')
        db_version = cur.fetchone()
        print(db_version)
        conn.close()

    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.!')








