students = ['태연', '성진', '하늘', '정현', '진우']

for number, name in enumerate(students):
    print('{}번의 이름은 {}입니다'.format(number, name))

print('-----------------------------')
stud_dict = {'{}번'.format(number + 1): name for number, name in enumerate(students)}
print(stud_dict)

print('------------------------------')
scores = [85, 90, 100, 75, 83]

for x, y in zip(students, scores):
    print(x, y)

score_dict = {x: y for x, y in zip(students, scores)}
print(score_dict)

print('------------------------------')

product_list = ['풀', '가위', '크레파스']
price_list = [800, 2500, 5000]
price_dict = {x: y for x, y in zip(product_list, price_list)}
print(price_dict)
