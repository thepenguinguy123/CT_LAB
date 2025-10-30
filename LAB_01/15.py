def factorial(n):
    if n < 0:
        return "Không tính được giai thừa cho số âm!"
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


m = int(input("Please enter a number: "))
print(factorial(m))