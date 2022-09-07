info = {'이름': '홍길동',
        '나이': 23,
        '직업': '회사원'}

infoList = ['홍길동', 23, '회사원']
print(infoList[2])
print(info['직업'])

dict1 = {'성적': [90, 80, 70], '이름': '김유신'}

print(dict1['성적'][0], dict1['이름'])

dict2 = {'1월': 31, '2월': 28, '3월': 31}
print(dict2['1월'])

print('-----------------------')
list1 = [1, 2, 3, 4, 5]
list1[2] = 100
print(list1[2])
list1.append(6)
list1.remove(4)
del (list1[3])

print('------------------------')
dict3 = {'이름': '홍길순', '나이': 33}
dict3['나이'] = 23  # 나이 수정
dict3['직업'] = '학생'
del (dict3['나이'])  # 나이 삭제
print(dict3)

print('------------------------')
list2 = [1, 2, 3, 4, 5, 6, 7, 8]
dict4 = {'1월': 31, '2월': 29, '3월': 31, '4월': 30}

# a = list2.pop(2)  # 해당 인덱스의 값을 삭제하고 반환 함
# print(list2)
# print(a)
# print(dict4.pop('2월'))
# print(dict4)

print('------------------------')

for month in dict4.keys():
    print(month)
    print(dict4[month])

print('------------------------')
for days in dict4.values():
    print(days)

print('------------------------')
# key,value 동시 출력 =>items()
for key, value in dict4.items():
    print('key=', key)
    print('value=', value)

print('------------------------')
days_in_month = {'1월': 31, '2월': 28, '3월': 31, '4월': 30, '5월': 31, }
for key, value in days_in_month.items():
    print("{}은 {}일이 있습니다.".format(key, value))

print('------------------------')
if '1월' in days_in_month.keys():
    print('1월이 dict에 있습니다.')

if 28 in days_in_month.values():
    print('28일이 dict에 있습니다.')

# days_in_month.clear()  # dict 내용 모두 삭제
# print(days_in_month)
#
# list2.clear()  # 리스트 내용 모두 삭제
# print(list2)
print('------------------------')
list2.pop(2)
print(list2)

print(list2[2])

print('------------------------')
list3 = [1, 2, 3, 4]
list4 = [4, 5, 6, 7]
list5 = list3 + list4  # 리스트의 +연산자는 합집합의 의미는 아니다.
print(list5)

print('------------------------')
dict5 = {1: 100, 2: 200, 3: 300}
dict6 = {1: 1000, 2: 2000, 4: 4000}
dict5.update(dict6)  # 두개의 dict합칠때는 update사용
print(dict5)

print('------------------------')
dict8 = {'1월 월급': 100, '2월 월급': 200, '4월 월급': 300}
dict9 = {'1월 월급': 150, '3월 월급': 180}

dict8.update(dict9)
print(dict8)

print('------------------------')


def check_and_clear(box):
    if '불량품' in box.keys():
        print('불량품이 있으면 box 를 clear합니다.')
        box.clear()


dict10 = {'불량품': 10, '정상품': 50, '수출품': 100}
check_and_clear(dict10)

print(dict10)


print('------------------------')

products = {'풀': 800, '딱풀': 1200, '색종이': 1000, '색연필': 5000, '스케치북': 800}
catalog = {'겨울용 실내화': 12000, '잠자리채': 8000, '딱풀': 1400}

products.update(catalog)
print(products)
