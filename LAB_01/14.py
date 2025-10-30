def describe_person(*args, **kwargs):
    print("Thông tin cá nhân:")
    for key, value in kwargs.items():
        print(f"  {key}: {value}")

    print()
    print("Sở thích:")
    for hobby in args:
        print(f"  - {hobby}")
   

describe_person("đọc sách", "chơi game", "du lịch", name="Jack", age=20, city="Đà Nẵng")
