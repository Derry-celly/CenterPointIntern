import csv

import xarray.core.dataset

file1 = open('/Users/derrickchen/Documents/圆心科技/project_2/file_1', 'r')
data1 = list(csv.reader(file1, delimiter = ','))

file1.close()

file2 = open('/Users/derrickchen/Documents/圆心科技/project_2/file_2', 'r')
data2 = list((csv.reader(file2, delimiter=',')))
file2.close()

id_1 = [info1 for info1 in data1[1:]]
id_2 = [info2 for info2 in data2[1:]]

def split(iter):
    return str(iter).split(',')

info1 = map(split, id_1)
info2 = map(split, id_2)
#print(list(info1))
#a = (''.join(map(str, info1)))
#b = (''.join(map(str, info2)))


def compare(iter1, iter2):
    for item1 in iter1:
        for item2 in iter2:
            if item1 == item2:
                print(item1)

final = map(compare, split(list(info1)), split(list(info2)))
print(list(final))