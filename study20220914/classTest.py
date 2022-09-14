# 삼각형 클래스 만들기
# 초기값으로 밑변, 높이르 입력해서 인스턴스 생성
# 삼각형의 면적을 출력하는 메서드 존재
# 인스턴스를 2개 생성하고 각각 밑변 10 , 높이 20
# 밑변 20, 높이 40인 삼각형의 면적 출력

class Triangle:
    def __init__(self, w, h):
        print('초기값 밑변 {}, 높이 {}'.format(w, h))
        self.w = w
        self.h = h

    def triangleArea(self):
        area = self.w * self.h / 2
        return area


triangle1 = Triangle(10, 20)
triangle2 = Triangle(20, 40)
print(triangle1.triangleArea())
print(triangle2.triangleArea())

print('-----------------------')


# 사직연사 클래스 만들기
# 두 개의 수를 초기값으로 입력하여 인스턴스 생성
# 사칙연산을 하는 메서드 4개 생성
# 20,10의 사칙연산 결과를 출력하도록 프로그램 작성

class Op:
    def __init__(self, a, b):
        print('초기값 {},{}'.format(a, b))
        self.a = a
        self.b = b

    def plus(self):
        add = self.a + self.b
        return add

    def minus(self):
        minus = self.a - self.b
        return minus

    def multi(self):
        mul = self.a * self.b
        return mul

    def div(self):
        div = self.a / self.b
        return div


op = Op(20, 10)
print(op.plus())
print(op.minus())
print(op.multi())
print(op.div())
