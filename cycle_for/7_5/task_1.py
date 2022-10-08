num = int(input())

while num != 0:
    last = num % 10
    print(last)
    num //= 10
