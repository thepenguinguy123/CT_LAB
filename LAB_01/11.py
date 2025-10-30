n = int(input("Please enter a number: "))
ans = 0
while True:
    ans += n
    if n == 0:
        break
    n = n - 1
print(ans)