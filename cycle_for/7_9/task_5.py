n = int(input())

while n > 9:
    dig_sum = 0
    while n != 0:
        dig_sum += n % 10
        n //= 10
    n = dig_sum
print(n)
