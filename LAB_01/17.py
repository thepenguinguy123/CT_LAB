with open("data.txt", "w") as f:
    students = ["An", "Jack", "Jayce", "Leona"]
    for name in students:
        f.write(name + "\n")
with open("data.txt", "r") as f:
    for x in f:
        print(x.strip())