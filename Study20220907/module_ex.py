import math
import random


print(math.pi)  # 파이값(소수점15자리)

area = 10 * 10 * math.pi  # 원의 면적
print(math.floor(area))  # 소수점 뒤 없앰

print('--------------------------')
gameNumber = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

user = input('"low" 또는 "high"를 입력 하세요:')
computer = random.choice(gameNumber)
# gameNumber 리스트 1~10중에서 1개 랜덤 선택

if computer >= 5:
    gameState = 'high'
else:
    gameState = 'low'
print('컴퓨터가 선택한 숫자는 {}입니다.'.format(computer))
if user == gameState:
    print('성공')
else:
    print('실패')

print('--------------------------')


