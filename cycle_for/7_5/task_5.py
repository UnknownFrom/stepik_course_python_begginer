num = int(input())

while num // 10 > 9:
    last = num % 10
    num //= 10
print(num % 10)
