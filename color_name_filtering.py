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
colors['블랙']=['black','블랙','검정','BK','먹색','블렉','흑색']
colors["블루"]=["blue","파랑","블루",'청','파란']
colors["레드"]=["red","빨강","레드"]
colors['그린']=['green','초록','그린','GN','녹색']
colors['옐로우']=['yellow','노란','옐로우','엘로우','노랑']
colors['핑크']=['pink','핑크']
colors['오렌지']=['orange','오렌지','OR']
colors['브라운']=['brown','브라운','갈색','밤색','벽돌','브릭','brick','Brick','BRICK']
colors['화이트']=['white','화이트','흰색','WH','백색']
colors['그레이']=['gray','그레이','grey','Grey','GREY','재색']
colors['퍼플']=['violet','보라','바이올렛','바이올랫','purple','Purple','PURPLE','퍼플','자주색']


colors['오트밀']=['oatmeal','오트밀']
colors['올리브']=['olive','올리브']

colors['세피아']=['sepia','세피아']
colors['코랄']=['coral','코랄']
colors['라일락']=['lilac','라일락']
colors['크림']=['cream','크림']
colors['레몬']=['lemon','레몬']
colors['체리']=['cherry','체리']
colors['피치']=['peach','피치','복숭아']
colors['차콜']=['charcoal','차콜','챠콜']
colors['머스타드']=['mustard','머스타드','겨자','머스터드']
colors['와인']=['wine','와인']
colors['코코아']=['cocoa','코코아']
colors['민트']=['mint','민트','MT']
colors['네이비']=['navy','네이비']
colors['베이지']=['beige','베이지','배이지']
colors['아이보리']=['ivory','아이보리','IV']
colors['남색']=['indigo','남색','인디고','곤색']
colors['카키']=['khaki','카키','KH']
colors['틸']=['teal','틸']
colors['버건디']=['burgandy','버건디']
colors['카멜']=['camel','카멜']
colors['골드']=['gold','금','골드']
colors['실버']=['silver','실버','은']
colors['소라']=['sora','소라']
colors['다홍']=['crimson','다홍']
colors['데님']=['denim','데님']
colors['라임']=['lime','라임']
colors['로즈']=['rose','로즈']
colors['마젠타']=['magenta','마젠다','마젠타']
colors['모카']=['moka','모카']
colors['카라멜']=['caramel','카라멜','케러멜']
##?
colors['연청']=['light blue','연청']
colors['연보라']=['lavender','라벤더','라벤다']
### 수식언 정리
modifi={}
modifi['스카이']=['sky','스카이','하늘']
modifi['다크']=['dark','다크']
modifi['라이트']=['light','라이트','연']
modifi['멜란지']=['melange','멜란지']
modifi['미들']=['middle','중']
modifi['체크']=['check','체크']

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
    if line[2]=='패션잡화':
        check2=1

    if check2==1 or check3==1:
        wr.writerow(line)
        product_num+=1

print(product_num)
f.close()
fo.close()
debug=0
