class Shape:

    def __init__(self, num1, num2):  # 초기화자, 생성자 ->객체를 생성할때 자동으로 실행 메서드

        self.width = num1
        self.height = num2

    def area(self):
        area = self.width * self.height
        print('면적{}'.format(area))

    def test(self):
        print('부모 클래스의 test메소드')


class Square(Shape):
    shape1 = Shape(10, 20)  # 클래스로 객체(인스턴스)를 생성
    shape1.area()

    def subArea(self):
        print('자식 클래스의  메서드 호출')
        sum = self.width + self.height
        print(sum)


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def circleArea(self):
        area = self.radius * self.radius * 3.14
        print(area)

    def area(self):
        print('부모 클래스의 area 메서드를 오버 라이딩 하였습니다.')

    def test(self):
        print('자식의  test 메서드를 오버라이딩 하였습니다.')
        super().test()  # 부모의 test메소드를 호출


class Triangle(Shape):
    def __init__(self, number, width, height):
        self.number = number
        super().__init__(width, height)
        # self.width = width
        # self.height = height

    def tri(self):
        print('저는 삼각형 입니다. number값은 {}입니다'.format(self.number))


tri1 = Triangle(1000, 20, 30)
tri1.area()
tri1.tri()

print('-------------------')

square1 = Square(50, 60)
square1.area()
square1.subArea()

print('-------------------')

circle1 = Circle(10)
circle1.circleArea()
circle1.area()
circle1.test()
