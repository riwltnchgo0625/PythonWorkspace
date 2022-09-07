tuple1 = (1, 2, 3, 4, 5)  # 튜플 선언1
tuple2 = 1, 2, 3, 4, 5  # 튜플 선언2

print(type(tuple2))  # type확인
print('------------------------------')

for tuple in tuple1:
    print(tuple)
print('------------------------------')
for tuple in range(len(tuple1)):
    print(tuple)

print('------------------------------')
list1 = [1, 2, 3, 4, 5]
list1[1] = 100
del list1[1]
print(list1)

print('------------------------------')
# tuple은 한번 만들면 수정 불가
# tuple1[1] = 100
# print(tuple1)

print('------------------------------')

a, b = 1, 2
print(a)
print(b)

c = (3, 4)  # 튜플 c 선언

d, e = c  # 언패킹
print(d)
print(e)

print('------------------------------')

# 패킹
f = 10
g = 20
h = f, g
print(h)

print(type(h))
