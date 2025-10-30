import json
json_str = '{"name": "Mai", "age": 25, "city": "Hanoi"}'
data = json.loads(json_str)
print("Tên:", data["name"])
print("Tuổi:", data["age"])
print("Thành phố:", data["city"])
json_re = json.dumps(data)
print(json_re)