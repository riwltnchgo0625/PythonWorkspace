# def mul(x, y, z):
#     mul1 = x * y * z
#     return mul1
#
#
# temp = mul(10, 20, 30)
# print(temp)

# score = input('점수를 입력하세요: ') #input은 기본적으로 str으로 저장함
# score = int(score)
#
# print(score+100)

#list
list1 = [100, 90, 40, 60, 70]
list1.append(200)  # 리스트 끝에 숫자 추가하기
print(list1)

list2 = [10, 52, 58, 88]
print(list2)

#in연산
ownership = 100 in list1
print(ownership)

if 100 in list1:
    print("100이 list1에 있습니다.")