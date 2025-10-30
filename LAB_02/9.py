class Salary:
    def __init__(self, pay, bonus):
        self.pay = pay
        self.bonus = bonus

    def total(self):
        return self.pay + self.bonus
    
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary 

    def total_compensation(self):
        return self.salary.total()

salary1 = Salary(5000, 1000)
salary2 = Salary(7000, 1500)

emp1 = Employee("Alice", salary1)
emp2 = Employee("Bob", salary2)

print(f"{emp1.name}'s total compensation: {emp1.total_compensation()} USD")
print(f"{emp2.name}'s total compensation: {emp2.total_compensation()} USD")
