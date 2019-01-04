import numpy as np
import csv

def preprocessing_Master():
    """
    06.Master 파일 preprocessing
    * 06. Master 파일은 모든 제품에대한 정보를 포함함 *
    1) '여성의류' & '패션잡화'만 따로 저장
    2) '남성', '유아', '아동' 의 키워드를 가지고 있는 제품은 제외

    저장파일 이름은 06.Master_로 저장
    """
    input_file_name = '제5회 Big Data Competition-분석용데이터-06.Master.csv'
    out_file_name = '06.Master_.csv'

    input_file = open(input_file_name, 'rt', encoding='UTF8')
    reader = csv.reader(input_file)
    data = list(reader)

    out_file = open(out_file_name, 'w', encoding='UTF8', newline='')
    writer = csv.writer(out_file)

    line_num = 0
    product_num = 0
    for line in data:
        check = 0
        if line_num == 0:
            writer.writerow(line)

        if line[2] in ['여성의류', '패션잡화']:
            for s in line:
                if "남성" in s or "유아" in s or "아동" in s:
                    check = 1
            if check == 0:
                line_ = line[1].split(' - ')
                line[1] = line_[-1]
                line.append(line_[0:-1])
                writer.writerow(line)
                product_num += 1
        line_num += 1

    print("Number of master : ", product_num)
    input_file.close()
    out_file.close()

def preprocessing_Product():
    """
    01.Product 파일 preprocessing
    * 01. Product 파일은 모든 구매내역에대한 정보를 포함함 *
    1) 'Hit' 정보 제외하고 저장

    저장파일 이름은 01.Product_로 저장
    """
    input_file_name = '제5회 Big Data Competition-분석용데이터-01.Pruduct.csv'
    out_file_name = '01.Product_.csv'

    input_file = open(input_file_name, 'rt', encoding='UTF8')
    reader = csv.reader(input_file)
    data = list(reader)

    out_file = open(out_file_name, 'w', encoding='UTF8', newline='')
    writer = csv.writer(out_file)

    line_num = 0
    for line in data:
        line_ = [line[0], line[1], line[3], line[-2], line[-1], line[4]]
        writer.writerow(line_)
        line_num += 1

    print("Number of Product : ", line_num)
    input_file.close()
    out_file.close()

def preprocessing_Master_list():
    """
    06.Master_ 파일에서 제품 코드만 list화
    * 06. Master_ 파일은 '여성의류' & '패션잡화' ('남성', '유아', '아동' 제외)제품에대한 정보를 포함함 *
    1) 제품 코드만 저장

    저장파일 이름은 06.Master_list로 저장
    """
    input_file_name = '06.Master_.csv'
    out_file_name = '06.Master_list.csv'

    input_file = open(input_file_name, 'rt', encoding='UTF8')
    reader = csv.reader(input_file)
    data = list(reader)

    out_file = open(out_file_name, 'w', encoding='UTF8', newline='')
    writer = csv.writer(out_file)

    line_num = 0
    list_ = []
    for line in data:
        if line_num != 0:
            list_.append(line[0])
        line_num += 1
    writer.writerow(list_)
    input_file.close()
    out_file.close()

def preprocessing_Product_():
    """
        01.Product_ 파일에서 '여성의류' & '패션잡화' ('남성', '유아', '아동' 제외)제품 구매내역만 추출하여 저장

        저장파일 이름은 01.Product__로 저장
    """
    input_file_name_1 = '01.Product_.csv'
    input_file_name_2 = '06.Master_list.csv'
    out_file_name = '01.Product__.csv'

    input_file_1 = open(input_file_name_1, 'rt', encoding='UTF8')
    reader_1 = csv.reader(input_file_1)
    data_1 = list(reader_1)

    input_file_2 = open(input_file_name_2, 'rt', encoding='UTF8')
    reader_2 = csv.reader(input_file_2)
    data_2 = list(reader_2)

    out_file = open(out_file_name, 'w', encoding='UTF8', newline='')
    writer = csv.writer(out_file)

    line_num = 0
    # a = data_2[0]
    for line in data_1:
        if line[2] in data_2[0]:
            writer.writerow(line)
            line_num += 1
            print(line_num)

    input_file_1.close()
    input_file_2.close()
    out_file.close()

if __name__ == "__main__":
    # preprocessing_Master()
    # preprocessing_Product()
    # preprocessing_Master_list()
    preprocessing_Product_()
