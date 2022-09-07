list1 = [1, 2, 3, 4, 5]
a = 10
for i in list1:
    print(i)

print('-------------------------------')
list2 = ['가위', '바위', '보']
for a in list2:
    print(a)

print('-------------------------------')
for i in range(10):
    print(i + 1)

print('-------------------------------')
list3 = ['호랑이', '고양이', '강아지', '거북이']
for i in range(len(list3)):  # 리스트의 길이를 자동으로 측정
    # len(): 리스트의 원소의 개수를 반환하는 함수
    print(list3[i])

print('-------------------------------')
for i, animal in enumerate(list3):  # 인덱스와 값을 동시에 뽑을 수 있음
    print(i)
    print('*******')
    print(animal)
    print('*******')

print('-------------------------------')
for i, animal in enumerate(list3):
    print('list3 리스트의 {}번째 원소는 {}입니다'.format(i + 1, animal))
