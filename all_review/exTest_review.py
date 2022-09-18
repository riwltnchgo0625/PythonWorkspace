# 리스트에 있는 글자열 앞글자만 추출
animal_list = ['cat', 'dog', 'lion']

for animal in animal_list:
    print(animal[0])

# 가나 나다 다라
list1 = ['가', '나', '다', '라']

for i in range(len(list1)):
    print('{}{}'.format(list1[i], list1[i + 1]))
