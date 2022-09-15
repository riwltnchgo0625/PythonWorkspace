list1 = [1, 2, 3]

for i in range(4):
    print(i)

print('--------------------')

rainbow = ["빨", "주", "노", "초", "파", "남", "보"]
for i in range(len(rainbow)):
    color = rainbow[i]
    print('{}번째 색은 {}'.format(i + 1, color))

print('--------------------')

rainbow = ["빨", "주", "노", "초", "파", "남", "보"]
for i, color in enumerate(rainbow):
    print('{}번째 색은 {}'.format(i + 1, color))

print('--------------------')

days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
for i, day in enumerate(days):
    print('{}월의 날짜 수는 {}일 입니다.'.format(i + 1, day))
