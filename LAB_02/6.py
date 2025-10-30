import math as m
class Shape:
    def __init__(self):
        pass
    def area(self):
        pass
class Circle(Shape):
    def __init__(self, r):
        super().__init__()
        self.r = r
    def area(self):
        return (self.r ** 2) * m.pi
class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__()
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

shapes = [
    Circle(3),
    Rectangle(4, 5),
    Circle(2),
    Rectangle(3, 6)
]

total_area = 0
for shape in shapes:
    print(f"{shape.__class__.__name__} area: {shape.area():.2f}")
    total_area += shape.area()

print(f"Total area of all shapes: {total_area:.2f}")