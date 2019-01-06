import numpy as np
import csv

### 상품 중분류 나누기
file_name='product_list.csv'

f = open(file_name, 'rt', encoding='UTF8')
reader = csv.reader(f)
datas = list(reader)

out_file_name1 = 'purchase_list_category_1.csv'
fo = open(out_file_name1, 'w', encoding='UTF8', newline='')
wr = csv.writer(fo)

check = 0
category_num = 0
category,num={},0

for line in datas:
    check = 0
    line_ = line[2] +','+ line[3]+','+ line[4]
    if not(line_ in category):
        category[line_]=num
        wr.writerow([line[2],line[3],line[4],num])
        num+=1
        category_num += 1

print(category_num)
f.close()
fo.close()

debug=0
