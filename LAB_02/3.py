class Student:
    def __init__(self, name, grade = 0):
        self.name = name
        self.__grade = grade
    def set_grade(self, grade):
        if 0 <= grade <= 100:
            self.__grade = grade
        else:
            raise ValueError("Grade must be between 0 and 100.")
    def get_grade(self):
        return self.__grade
student1 = Student("Alice")
student2 = Student("Bob")
student3 = Student("Charlie")

student1.set_grade(85)
student2.set_grade(92)

print(f"{student1.name}'s grade: {student1.get_grade()}")
print(f"{student2.name}'s grade: {student2.get_grade()}")

try:
    student3.set_grade(120)
except ValueError as e:
    print(f"Error for {student3.name}: {e}")