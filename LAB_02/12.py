from abc import ABC, abstractmethod
class AbstractAnimal(ABC):
    @abstractmethod
    def speak(self):
        pass
class Dog(AbstractAnimal):
    def speak(self):
        print("Woof! Woof!")

dog = Dog()
dog.speak()
