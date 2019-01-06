import numpy as np
import csv

### 상품 색깔찾기
file_name='product_list.csv'

f = open(file_name, 'rt', encoding='UTF8')
reader = csv.reader(f)
datas = list(reader)

out_file_name1 = 'purchase_list_colorfiltering.csv'
fo = open(out_file_name1, 'w', encoding='UTF8', newline='')
wr = csv.writer(fo)

### 색깔 리스트
colors={}
colors['블랙']=['black','블랙','검정','BK']
colors["블루"]=["blue","파랑","블루",'청']
colors["레드"]=["red","빨강","레드"]
colors['그린']=['green','초록','그린','GN']
colors['옐로우']=['yellow','노란','옐로우','엘로우','노랑']
colors['핑크']=['pink','핑크']
colors['오렌지']=['orange','오렌지','OR']
colors['브라운']=['brown','브라운','갈색']
colors['화이트']=['white','화이트','흰색','WH']
colors['그레이']=['gray','그레이','grey','Grey','GREY']
colors['퍼플']=['violet','보라','바이올렛','바이올랫','purple','Purple','PURPLE','퍼플']

colors['코랄']=['coral','코랄']
colors['라일락']=['lilac','라일락']
colors['크림']=['cream','크림']
colors['레몬']=['lemon','레몬']
colors['체리']=['cherry','체리']
colors['피치']=['peach','피치','복숭아']
colors['차콜']=['charcoal','차콜','챠콜']
colors['머스타드']=['mustard','머스타드']
colors['와인']=['wine','와인']
colors['코코아']=['cocoa','코코아']
colors['민트']=['mint','민트','MT']
colors['네이비']=['navy','네이비']
colors['베이지']=['beige','베이지','배이지']
colors['아이보리']=['ivory','아이보리','IV']
colors['남색']=['indigo','남색','인디고']
colors['카키']=['khaki','카키','KH']
colors['틸']=['teal','틸']
##?
colors['연청']=['light blue','연청']
colors['연보라']=['lavender','라벤더']
### 수식언 정리
modifi={}
modifi['스카이']=['sky','스카이','하늘']
modifi['다크']=['dark','다크']
modifi['라이트']=['light','라이트','연']
modifi['멜란지']=['melange','멜란지']
modifi['미들']=['middle','중']

###색깔 영어(capitalize(), upper() 추가)
for color in colors:
    co_= colors[color][0]
    colors[color].append(co_.capitalize())
    colors[color].append(co_.upper())

for modi in modifi:
    modi_=modifi[modi][0]
    modifi[modi].append(modi_.capitalize())
    modifi[modi].append(modi_.upper())

###
check = 0
product_num = 0

for line in datas:
    check=0
    check2=0 #색상유무 판별
    check3=0 #수식유무 판별
    line.append('')
    for modi in modifi:
        for modi_ in modifi[modi]:
            if modi_ in line[1]:
                line[-1]+=modi
                check3=1
                break

    for color in colors:
        for co_ in colors[color]:
            if co_ in line[1]:
                line[-1]+=color
                check2=1
                break

    if check2==1 or check3==1:
        wr.writerow(line)
        product_num+=1

print(product_num)
f.close()
fo.close()
debug=0
