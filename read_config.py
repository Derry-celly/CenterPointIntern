import configparser
from configparser import ConfigParser


# Write database information into an ini con.json file.
# 将数据库基础配置信息写入ini配置文件。

config = configparser.ConfigParser()
config['database'] = {
    'host': 'localhost',
    'port': 5432,
    'user': 'postgres',
    'database': 'insurance',
    'password': '100910',
}
config['business'] = {
    'columns': 'insurance_id, '
               'channel_i_name, '
               'channel_i_code, ',

    'numbers': 10,
}

# Read ini con.json file
# 读数据库配置文件

def read_config(filename = 'config.ini', section = 'database'):
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

print(read_config())


















#with open('con.json.ini', 'w+') as file:
 #   con.json.write(file)










