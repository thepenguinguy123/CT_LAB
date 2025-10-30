class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage
class Bus(Vehicle):
    def __init__(self, max_speed, mileage, passengers):
        super().__init__(max_speed, mileage)
        self.passengers = passengers

bus1 = Bus(120, 25000, 50)
print(f"Max speed: {bus1.max_speed} km/h")
print(f"Mileage: {bus1.mileage} km")
print(f"Number of passengers: {bus1.passengers}")