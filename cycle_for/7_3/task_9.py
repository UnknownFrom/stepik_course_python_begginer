n = int(input())
total = 0

for i in range(1, n + 1, 2):
    total += i

for i in range(2, n + 1, 2):
    total -= i

print(total)
