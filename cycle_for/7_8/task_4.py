import math

n = int(input())

for i in range(1, n + 1):
    if i <= math.ceil(n / 2):
        print('*' * i)
    else:
        print('*' * (n + 1 - i))
