num = int(input())
largest = -1
smallest = 10
while num != 0:
    last = num % 10
    if last > largest:
        largest = last
    if last < smallest:
        smallest = last
    num //= 10

print(f'Максимальная цифра равна {largest}')
print(f'Минимальная цифра равна {smallest}')
