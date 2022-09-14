for number in range(5):
    print(number)

print("--------------")

i = 0
while i < 10:
    print(i)
    i = i + 1

print("--------------")

# 예외처리 try-except
comNumber = input('컴퓨터가 생각한 숫자를 입력하세요')
try:
    comNumber = int(comNumber)
    print(comNumber)
except:
    print('입력은 숫자만 해주세요')

print("--------------")


