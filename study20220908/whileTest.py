print('1. 성적보기')
print('2. 수강확인')
print('1. 프로그램 종료')

menuNumber = input('원하는 메뉴의 번호를 선택해주세요 >>')

while menuNumber not in ['1', '2', '3']:
    print('잘못된 메뉴 번호 입니다. 다시 입력해주세요')
    print('-------------------')
    print('1. 성적보기')
    print('2. 수강확인')
    print('1. 프로그램 종료')
    print('-------------------')
    menuNumber = input('원하는 메뉴의 번호를 선택해주세요 >>')

    print('선택하신 메뉴번호는 {}입니다'.format(menuNumber))
