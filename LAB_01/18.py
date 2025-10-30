try:
    n = float(input("Nhap so chia: "))
    m = float(input("Nhap so bi chia: "))
    result = n / m
    print(f"Ket qua = {result}")
except ZeroDivisionError:
    print("Error: So bi chia phai khac khong!")
except ValueError:
    print("Error: Vui long nhap so!")
else:
    print("Phep chia thuc hien thanh cong.")
finally:
    print("Ket thuc chuong trinh.")