class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    def get_info(self):
        return f"{self.year} {self.make} {self.model}"

car1 = Car("Toyota", "Corolla", 2020)
car2 = Car("Honda", "Civic", 2022)
car3 = Car("Tesla", "Model 3", 2024)

print(car1.get_info())
print(car2.get_info())
print(car3.get_info())
        