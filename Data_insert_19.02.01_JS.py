import numpy as np
import csv

def preprocessing_Product_2():
    """
        Product_Base의 제품코드에 해당되는 정보를 06.Master_color 파일에서 가져오기
    """

    input_file_name_1 = '01.Product__.csv'
    input_file_name_2 = '06.Master_color_1.csv'
    out_file_name = '07.P+M_.csv'

    input_file_1 = open(input_file_name_1, 'rt', encoding= "ISO-8859-1")# encoding='utf-8')
    reader_1 = csv.reader(input_file_1)
    data_1 = list(reader_1)

    input_file_2 = open(input_file_name_2, 'rt', encoding='UTF8')
    reader_2 = csv.reader(input_file_2)
    data_2 = list(reader_2)

    out_file = open(out_file_name, 'w', encoding='UTF8', newline='')
    writer = csv.writer(out_file)

    line_num =0
    '''기존 코드'''
    # for line1 in data_1:
    #     for line2 in data_2:
    #         if line1[2] == line2[0]:
    #             line1.append(line2[-1])
    #             writer.writerow(line1)
    #             line_num += 1
    #             print(line_num)

    '''수정 코드'''
    dict={}

    for line2 in data_2:
        dict[line2[0]]=line2[-1]
    print('Complete making dict')

    error_num=0
    for line1 in data_1:
        try:
            product_color=dict[line1[2]]
        except:
            product_color=None
            error_num+=1
        line1.append(product_color)
        writer.writerow(line1)
        line_num+=1
        print(line_num)
    print(error_num)
    '''수정 코드 END'''

    input_file_1.close()
    input_file_2.close()
    out_file.close()

def preprocessing_Product_3():
    """
        P+M의 에 해당되는 정보를 04.Custom 파일에서 가져오기
    """

    input_file_name_1 = '07.P+M_.csv'
    input_file_name_2 = '06.Master_.csv'
    out_file_name = '07.P+M_1.csv'

    input_file_1 = open(input_file_name_1, 'rt', encoding='utf-8')
    reader_1 = csv.reader(input_file_1)
    data_1 = list(reader_1)

    input_file_2 = open(input_file_name_2, 'rt', encoding='UTF8')
    reader_2 = csv.reader(input_file_2)
    data_2 = list(reader_2)

    out_file = open(out_file_name, 'w', encoding='UTF8', newline='')
    writer = csv.writer(out_file)

    line_num =0
    '''기존코드'''
    # for line1 in data_1:
    #     for line2 in data_2:
    #         if line1[2] == line2[0]:
    #             line1.append(line2[2])
    #             line1.append(line2[3])
    #             line1.append(line2[4])
    #             writer.writerow(line1)
    #             line_num += 1
    #             print(line_num)

    '''수정코드'''
    dict = {}

    for line2 in data_2:
        dict[line2[0]] = (line2[2],line2[3],line2[4])
    print('Complete making dict')

    error_num = 0
    for line1 in data_1:
        try:
            custom = dict[line1[2]]
        except:
            product_color = (None,None,None)
            custom += 1
        line1.append(custom[0])
        line1.append(custom[1])
        line1.append(custom[2])
        writer.writerow(line1)
        line_num += 1
        print(line_num)
    print(error_num)
    '''수정 코드 END'''

    input_file_1.close()
    input_file_2.close()
    out_file.close()

def preprocessing_Product_4():
    """
        P+M의 ID에 해당되는 정보를 04.Custom 파일에서 가져오기
    """
    input_file_name_1 = '07.P+M_1.csv'
    input_file_name_2 = '제5회 Big Data Competition-분석용데이터-04.Custom.csv'
    out_file_name = '07.P+M_2.csv'

    input_file_1 = open(input_file_name_1, 'rt', encoding='utf-8')
    reader_1 = csv.reader(input_file_1)
    data_1 = list(reader_1)

    input_file_2 = open(input_file_name_2, 'rt', encoding='UTF8')
    reader_2 = csv.reader(input_file_2)
    data_2 = list(reader_2)

    out_file = open(out_file_name, 'w', encoding='UTF8', newline='')
    writer = csv.writer(out_file)

    line_num =0
    '''기존 코드'''
    # for line1 in data_1:
    #     for line2 in data_2:
    #         if line1[0] == line2[0]:
    #             line1.append(line2[-2])
    #             line1.append(line2[-1])
    #             writer.writerow(line1)
    #             line_num += 1
    #             print(line_num)
    '''수정 코드'''
    dict = {}

    for line2 in data_2:
        dict[line2[0]] = (line2[-2],line2[-1])
    print('Complete making dict')

    error_num = 0
    for line1 in data_1:
        try:
            ID = dict[line1[0]]
        except:
            ID = (None,None)
            error_num += 1
        line1.append(ID[0])
        line1.append(ID[1])

        writer.writerow(line1)
        line_num += 1
        print(line_num)
    print(error_num)
    '''수정 코드 END'''

    input_file_1.close()
    input_file_2.close()
    out_file.close()

def preprocessing_Product_5():
    """
        P+M_1의 세션 ID에 해당되는 정보를 05.session 파일에서 가져오기
    """

    input_file_name_1 = '07.P+M_2.csv'
    input_file_name_2 = '제5회 Big Data Competition-분석용데이터-05.Session.csv'
    out_file_name = '07.P+M_3.csv'

    input_file_1 = open(input_file_name_1, 'rt', encoding='utf-8')
    reader_1 = csv.reader(input_file_1)
    data_1 = list(reader_1)

    input_file_2 = open(input_file_name_2, 'rt', encoding='UTF8')
    reader_2 = csv.reader(input_file_2)
    data_2 = list(reader_2)

    out_file = open(out_file_name, 'w', encoding='UTF8', newline='')
    writer = csv.writer(out_file)

    line_num =0
    '''기존 코드'''
    # for line1 in data_1:
    #     for line2 in data_2:
    #         if line1[1].zfill(8) == line2[1]:
    #             line1.append(line2[-3])
    #             line1.append(line2[-2])
    #             line1.append(line2[-1])
    #     writer.writerow(line1)
    #     line_num += 1
    #     print(line_num)

    '''수정 코드'''
    dict = {}

    line_num = 0
    error_num = 0
    for line2 in data_2:
        dict[line2[1]] = (line2[-1], line2[-2], line2[-3])
    print('Making dictionary complete')

    for line1 in data_1:
        try:
            session = dict[line1[1].zfill(8)]
        except:
            session = (None, None, None)
            error_num += 1
        line1.append(session[0])
        line1.append(session[1])
        line1.append(session[2])

        writer.writerow(line1)
        line_num += 1
        print(line_num)
    print(error_num)
    '''수정 코드 END'''

    input_file_1.close()
    input_file_2.close()
    out_file.close()

if __name__ == "__main__":
    # preprocessing_Product_2()
    # preprocessing_Product_3()
    # preprocessing_Product_4()
    preprocessing_Product_5()