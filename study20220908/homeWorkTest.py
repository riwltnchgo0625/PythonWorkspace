import random

# 과제
# 사용자로부터 수를 입력받아 컴퓨터가 생각한 수를 맞추는 게임

# [출력화면]
# 남은 출력 횟수 : 20
# 컴퓨터가 생각한 수를 맞춰보세요(1~99) >> 55
# 틀렸습니다. 컴퓨터의 수는 55보다 큰 수입니다.
# 남은 출력 횟수 : 19
# 컴퓨터가 생각한 수를 맞춰보세요(1~99) >> 60
# 정답입니다. 게임을 종료합니다.

# 몇번만에 맞췄는지 출력
# 남은 시도 횟수 : 20 19 18 ...0 이면 게임종료

chance = 20
count = 0
com_number = random.randint(1, 99)
print('남은 출력 횟수 :', chance)

while True:
    user = int(input('컴퓨터가 생각한 수를 맞춰 보세요 :'))

    if user == com_number:
        print('정답입니다. 게임을 종료합니다')
        break

    elif chance == 0:
        print("남은 횟수가 없습니다. 게임을 종료합니다.")
        break

    elif user > com_number:
        print('틀렸습니다. 컴퓨터의 수는 {}보다 작은 수 입니다'.format(user))
        count = count + 1
        chance = chance - 1
        continue
    else:
        print('틀렸습니다. 컴퓨터의 수는 {}보다 큰 수 입니다'.format(user))
        chance = chance - 1
        count = count + 1
        continue

print('남은 횟수 :', chance)
print('시도 횟수 :', count)
