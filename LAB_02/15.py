import math 
class Circle:
    def __init__(self, radius):
        self._radius = radius
    @property
    def radius(self):
        return self._radius
    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("Radius must be non-negative.")
        self._radius = value
    def area(self):
        return math.pi * (self._radius ** 2)

c = Circle(5)
print(f"Radius: {c.radius}")
print(f"Area: {c.area():.2f}")

c.radius = 10
print(f"New radius: {c.radius}")
print(f"New area: {c.area():.2f}")

try:
    c.radius = -3
except ValueError as e:
    print(f"Error: {e}")

        