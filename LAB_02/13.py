class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display_info(self):
        return f"Name: {self.name}, Salary: ${self.salary}"
    
class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    def display_info(self):
        base_info = super().display_info()
        return f"{base_info}, Department: {self.department}"
    
class Executive(Manager):
    def __init__(self, name, salary, department, stock_options):
        super().__init__(name, salary, department)
        self.stock_options = stock_options

    def display_info(self):
        base_info = super().display_info()
        return f"{base_info}, Stock Options: {self.stock_options}"

emp = Employee("Alice", 50000)
mgr = Manager("Bob", 80000, "Sales")
execu = Executive("Charlie", 120000, "Marketing", 5000)

print(emp.display_info())
print(mgr.display_info())
print(execu.display_info())