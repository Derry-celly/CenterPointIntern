import json
# Write con.json file in json format, which is mapping of English and Chinese names of lines.
# 写json格式配置文件，导入英语列名和中文列名映射。
'''dic = {
  "insurance_id": "保单号",
  "channel_i_name": "保险公司名",
  "channel_i_code": "保险公司号"

}

j_object = json.dumps(dic, indent = 3)
with open('/Users/derrickchen/Documents/圆心科技/Json', 'w') as f:
    f.write(j_object)'''

# Read json con.json file.
# 读配置文件中的映射。
def read_values(filename = '/Users/derrickchen/Documents/圆心科技/Json'):
    with open(filename) as jsonFile:
        data = json.load(jsonFile)
        #print(data)
        #print(data)


        # for value in data.values():
        #     print(value)
    return data


if __name__ == '__main__':
    print((read_values()))
