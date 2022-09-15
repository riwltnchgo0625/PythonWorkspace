# 한변의 길이가 1~10인 정사각형의 넓이를 원소로 가지는 리스트를 만드시오

areas = []  # 빈 리스트 생성

for i in range(1, 11):  # range(1,11) -> [1,2,3,4,5,6,7,8,9,10]

    # area = i* i
    # areas.append(area)
    areas = areas + [i * i]

print(areas)

print('--------------------------')

areas2 = [i * i for i in range(1, 11)]
print(areas2)

print('--------------------------')

areas3 = []
for i in range(1, 11):
    if i % 2 == 0:
        areas3 = areas3 + [i * i]

print(areas3)
print('---------------------------')

areas4 = [i * i for i in range(1, 11) if i % 2 == 0]
print(areas4)

print('---------------------------')

tupleList1 = [(i, j) for i in range(1, 11) for j in range(11, 21)]
print(tupleList1)  # 100개의 튜플이 원소인 리스트 생성

print('---------------------------')

list1 = [i for i in range(1, 101) if i % 8 == 0]
print(list1)
print('---------------------------')

# 구구단의 결과값을 원소로 가지는 리스트를 리스트 내포를 사용하여 작성
list2 = [(i * j) for i in range(2, 10) for j in range(1, 10)]
print(list2)
