list = [1, 2, 3, 5, 7, 2, 5, 237, 55]
for i in range(len(list)):
    if list[i] % 2 != 0:
        print(list[i])

print('--------------------------------------')

list2 = [1, 2, 3, 5, 7, 2, 5, 237, 55]
for i in list2:
    if i % 2 != 0:
        print(i)

print('--------------------------------------')

for i in range(len(list)):
    if list[i] % 2 == 0:
        continue
    print(list[i])

print('---------------------------------------')

sizes = [33, 35, 34, 37, 32, 35, 39, 32, 35, 29]
for i, size in enumerate(sizes):
    if size == 32:
        print("사이즈 32인 바지는 {}번째에 있다.".format(i+1))
        break

numbers = [(1, 2), (10, 0)]
for a, b in numbers:
    if b == 0:
        print("0으로 나눌 수는 없습니다.")
        continue
    print('{}를 {}로 나누면 {}'.format(a, b, a/b))