# 문제1) 하나의 딕셔너리를 입력받아 딕셔너리의 key 값을 화면에 출력하는 print_keys 함수를 정의하시오.
# 딕셔너리 키값만 출력
dic = {"이름": "김말똥", "나이": 30, "성별": 0}


def print_keys():
    for i in dic.keys():
        print(i)


print_keys()

print('--------------------------------------------------------------------')


# 문제2) 문자열을 입력받아 각 문자들로 구성된 리스트로 반환하는 make_list 함수를 정의하시오.
# abcd 입력

def make_list(string1):
    str1 = list(string1)
    return str1


print(make_list("abcd"))

print('--------------------------------------------------------------------')


# 문제3) 숫자로 구성된 하나의 리스트를 입력받아, 짝수들을 추출하여 리스트로 반환하는 pickup_even 함수를 구현하시오.
# 조건제시

def pickup_even(list1):
    list2 = [i for i in list1 if i % 2 == 0]
    return list2


print(pickup_even([3, 4, 5, 6, 7, 8]))
