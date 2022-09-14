## 오버라이드 예제

class Shape:

    def areaCalcu(self):
        pass


class Square(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def areaCalcu(self):
        area = self.width * self.height
        return area


class Triangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def areaCalcu(self):
        area = self.width * self.height * 0.5
        return area


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def areaCalcu(self):
        area = self.radius * self.radius * 3.14
        return area


square1 = Square(10, 20)
triangle1 = Triangle(20, 40)
circle1 = Circle(10)

print(square1.areaCalcu())
print(triangle1.areaCalcu())
print(circle1.areaCalcu())
