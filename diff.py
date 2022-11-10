from pandas.io.excel import ExcelWriter
import pandas as pd
import pandas as pd
import numpy as np
import xlwings as xw
import os
import csv
file1 = open('/Users/derrickchen/Documents/圆心科技/project_2/file_1', 'r')
data1 = list(csv.reader(file1, delimiter = ','))

file1.close()

file2 = open('/Users/derrickchen/Documents/圆心科技/project_2/file_2', 'r')
data2 = list(csv.reader(file2, delimiter=','))
file2.close()
#set_1 = set([i[0] for i in data1][1:])
#set_2 = set([i[0] for i in data2][1:])


id_1 = [info1 for info1 in data1[1:]]
id_2 = [info2 for info2 in data2[1:]]
for id1 in id_1:
    insurance_id1 = str(id1).split(',')[0]
    insured_amount1 = str(id1).split(',')[1]
    pay_amount1 = str(id1).split(',')[2]
    insured_total_amount1 = str(id1).split(',')[3]
    pay_status1 = str(id1).split(',')[4]
    insurance_product_code1 = str(id1).split(',')[5]
    findresult = False


    for id2 in id_2:
        insurance_id2 = str(id2).split(',')[0]
        insured_fee_amount2 = str(id2).split(',')[1]
        pay_amount2 = str(id2).split(',')[2]
        insured_total_amount2 = str(id2).split(',')[3]
        pay_status2 = str(id2).split(',')[4]
        insurance_product_code2 = str(id2).split(',')[5]

        if insurance_id1 == insurance_id2:
            findresult = True

            result1 = ''
            if insured_amount1 != insured_fee_amount2:
                result1 = result1 + insurance_id1 + ' : Insured amount from two files are not equal! ' + 'file1:' + insured_amount1 + ' file2:' + insured_fee_amount2
            if pay_amount1 != pay_amount2:
                result1 = result1 + 'Pay amount from two files are not equal!'
            if insured_total_amount1 != insured_total_amount2:
                result1 = result1 + 'Insured total amount from two files are not equal!'
            if pay_status1 != pay_status2:
                result1 = result1 + 'Pay status from two files are not equal!'
            if insurance_product_code1 != insurance_product_code2:
                result1 = result1 + 'Insurance product code from two files are not equal!'
            print(result1)
            id_2.remove(id2)
            break
    if findresult == False:
        result2 = ''
        result2 = result2 + 'Insurance information in file1 but not in file2: ' + insurance_id1


for info3 in id_2:
    result3 = 'Insurance information in file2 but not in file1:' + info3
    #print(result3)



with open('/Users/derrickchen/Documents/圆心科技/project_2/final_otput') as f:
    f.write(result1)
    f.write(result2)
    f.write(result3)






'''info1 = pd.read_csv('/Users/derrickchen/Documents/圆心科技/project_2/file_1')
info2 = pd.read_csv('/Users/derrickchen/Documents/圆心科技/project_2/file_2')

array1 = np.array(info1)
array2 = np.array(info2)

df_csv_1 = pd.DataFrame(array1, columns = ['insurance_id','insured_amount',
                                           'pay_amount','insured_total_amount',
                                           'pay_status','insurance_product_code'])
df_csv_1.sort_values(['insurance_id'],
                     axis = 0,
                    inplace = True)
df_csv_1.index += 1

df_csv_2 = pd.DataFrame(array2, columns = ['insurance_id','insured_fee_amount',
                                           'pay_amount','insured_total_amount',
                                           'pay_status','insurance_product_code'])

df_csv_2.sort_values(['insurance_id'],
                     axis = 0,
                    inplace = True)

df_csv_2.index += 1

df_csv_1.to_csv('d1sorted')
df_csv_2.to_csv('d2sorted')

df_csv_2['IDs'] = np.where(df_csv_1['insurance_id'].equals(df_csv_2['insurance_id']), True, False)
df_csv_2.index += 1
data = df_csv_1.eq(df_csv_2).to_string(index = True)

with open('/Users/derrickchen/Documents/圆心科技/project_2/output', 'w') as f:
    f.writelines(data)

df_2_id = df_csv_2['insurance_id']
df_2_id = pd.Series(df_2_id)
df_csv_1 = df_csv_1.assign(df_2_id = df_2_id.values)
#print(df_csv_1.to_string(index = False))

with open('/Users/derrickchen/Documents/圆心科技/project_2/ids', 'w') as f:
    f.write(df_csv_1.to_string(index = False))'''















            
















        



















