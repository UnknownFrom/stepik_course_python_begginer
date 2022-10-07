m = int(input())
p = int(input())
n = int(input())

for i in range(n):
    print(f'{i + 1} {m}')
    m += m * p / 100
