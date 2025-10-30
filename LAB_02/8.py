class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        if isinstance(other, Vector2D):
            return Vector2D(self.x + other.x, self.y + other.y)
        return NotImplemented  

    def __str__(self):
        return f"({self.x}, {self.y})"


v1 = Vector2D(3, 4)
v2 = Vector2D(1, 2)
v3 = Vector2D(-2, 5)

print(f"v1 = {v1}")
print(f"v2 = {v2}")
print(f"v3 = {v3}")

result = v1 + v2
print(f"v1 + v2 = {result}")

total = v1 + v2 + v3
print(f"v1 + v2 + v3 = {total}")

