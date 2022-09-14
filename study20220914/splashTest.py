list1 = ['사과', '수박', '참외', '배']

print(list1[1:3])  # 인덱스 1부터 3전까지 추출

print(list1[1:len(list1)])  # 인덱스 1부터 list1길이까지

print(list1[0:3])  # 처음부터 인덱스 3전 추출

print(list1[:3])  # 인덱스 처음부터 3전 추출

print(list1[0:])  # 처음부터 끝까지

print(list1[:])  # 리스트의 모든 원소 추출

print('-----------------')

rainbow = ["빨", "주", "노", "초", "파", "남", "보"]

red_colors = rainbow[0:3]
print(red_colors)

blue_colors = rainbow[4:7]
print(blue_colors)

print('-----------------')

list2 = list(range(10))
print(list2)

print(list2[4:9])
print(list2[4:9:2])  # [4,6,8]
print(list2[:9:3])  # [0,3,6]
print(list2[::2])  # [0,2,4,6,8]

print('----------------')

list3 = list(range(20))

new_list = list3[5:15:3]
print(new_list)

another_list = list3[5:18:4]
print(another_list)
