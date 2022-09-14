list1 = [10, 20, 30, 40, 50, 60]

try:
    print(list1.index(450))  # 해당 값의 인덱스를 반환
except:
    print('해당 값은 리스트 안에 없습니다.')

print("--------------")

list1.append(100)  # 한개의 값만 리스트에 추가 기능
print(list1)
list1.extend([200, 300, 400])  # 리스트에 리스트 추가
print(list1)
list1.insert(2, 150)  # 원하는 인덱스 위치에 새로운 값 추가
print(list1)

print("--------------")

list2 = [50, 40, 30, 100, 10]
list3 = list2.sort()
print(list3)

list2.sort()
list2.reverse()
print(list2)

print("--------------")
#
#
# def safe_index(a_list, value):
#     if value in a_list:
#         return a_list.index(value)
#     else:
#         return None
#
#     list3 = [1, 2, 3, 4, 5]
#     val = 3
#     index = safe_index(list3, val)
#     print(index1)
#
# def safe_index2(a_list, value):
#     try :
#         return None

list1 = [1, 2, 3, 4]

list1.insert(0, 8)  # 첫번째 자리에 '8'삽입
print(list1)

list1.sort()  # 오름차순 정리
print(list1)

list1.reverse()
print(list1)

print("--------------")


