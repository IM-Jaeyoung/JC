import numpy as np
import csv

### 구매내역
file_name = '제5회 Big Data Competition-분석용데이터-01.Pruduct.csv'

f = open(file_name, 'rt', encoding='UTF8')
reader = csv.reader(f)
datas = list(reader)

out_file_name = 'purchase_list.csv'
fo = open(out_file_name, 'w', encoding='UTF8', newline='')
wr = csv.writer(fo)

check = 0
product_num = 0
for line in datas:
    check = 0
    line_ = [line[0], line[3], line[-2], line[-1]]
    wr.writerow(line_)
    product_num += 1

print(product_num)
f.close()
fo.close()

###제품항목
file_name = '제5회 Big Data Competition-분석용데이터-06.Master.csv'

f = open(file_name, 'rt', encoding='UTF8')
reader = csv.reader(f)
datas = list(reader)

out_file_name = 'product_list.csv'
fo = open(out_file_name, 'w', encoding='UTF8', newline='')
wr = csv.writer(fo)

check = 0
product_num = 0
for line in datas:
    check = 0
    if line[2] == '여성의류' or line[2] == '패션잡화':
        for s in line:
            if "남성" in s:
                check = 1
            if "유아" in s:
                check = 1
            if "아동" in s:
                check = 1
        if check == 0:
            line_ = line[1].split(' - ')
            line[1] = line_[-1]
            line.append(line_[0:-1])
            wr.writerow(line)
            product_num += 1

print(product_num)
f.close()
fo.close()