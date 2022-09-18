# class로 사칙연산 만들기
class Op:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        add = self.a + self.b
        return add

    def minus(self):
        minus = self.a - self.b
        return minus

    def multi(self):
        multi = self.a * self.b
        return multi

    def div(self):
        div = self.a / self.b
        return div


op = Op(20, 10)

print(op.add())
print(op.minus())
print(op.multi())
print(op.div())

print('-------------------------------------')


# 도형 넓이 구하기
class Area:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def triangle(self):
        triArea = self.width * self.height * 0.5
        return triArea

    def square(self):
        squareArea = self.width * self.height
        return squareArea


area = Area(10, 20)
print(area.triangle())
print(area.square())

print('-------------------------------')


# 상속 클래스
class Car:
    def run(self):
        print('차가 달립니다.')


class Truck(Car):
    def load(self):
        print('짐을 실었습니다.')

    def run(self):
        print('트럭이 달립니다.')


class SportCar(Car):
    pass


car = Car()
truck = Truck()
sportCar = SportCar()
print(car.run())
print(truck.run())
print(truck.load())
print(sportCar.run())

print('------------------------------')