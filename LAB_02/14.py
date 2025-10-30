import json
class JsonSerializableMixin:
    def to_json(self):
        return json.dumps(self.__dict__)
class Product(JsonSerializableMixin):
    def __init__(self, name, price):
        self.name = name
        self.price = price

p1 = Product("Laptop", 1500)
print(p1.to_json())