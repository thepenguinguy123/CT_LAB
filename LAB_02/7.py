class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"{self.name} is {self.age} years old."
p1 = Person("Alice", 25)
p2 = Person("Bob", 30)
p3 = Person("Charlie", 22)

print(p1)
print(p2)
print(p3)