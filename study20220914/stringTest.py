list1 = [1, 2, 3, 4, 5]

print(list1[2])

str1 = 'korea'

print(str1[2])

if 3 in list1:
    print('ok')

if 'a' in str1:
    print('ok')

if 'K' in str1:
    print('ok')
    print(str1.index('k'))

print("--------------")

str2 = list('Japan')  # 문자열을 리스트로 변환
print(str2)

print("--------------")

str3 = '나는 학교에 갑니다'
str3_list = str3.split()  # 공백을 기준으로 리스트 생성
print(str3_list)

str4 = '나는/학교에/갑니다'
str4_list = str4.split('/')  # split에 구분자 넣어서 공백과 같은 효과 => 리스트로 변환
print(str4_list)

str5 = '/'.join(str4_list) # '/'로 구분되는 문자열로 변환
print(str5)
