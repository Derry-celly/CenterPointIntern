import configparser
from configparser import ConfigParser

# 写一个方法，读取配置文件中的业务需求部分。

def read_business(filename = 'con.json.ini', section = 'business'):
    parser = ConfigParser()
    parser.read(filename)

    db = {}

    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception('Section {} has not found in the {} file'.format(section, filename))

    return db

# print(read_business()['columns'])

