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

a = list2.pop(2)  # 해당 인덱스의 값을 삭제하고 반환 함
print(list2)
print(a)
print(dict4.pop('2월'))
print(dict4)

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

days_in_month.clear()  # dict 내용 모두 삭제
print(days_in_month)

list2.clear()  # 리스트 내용 모두 삭제
print(list2)
