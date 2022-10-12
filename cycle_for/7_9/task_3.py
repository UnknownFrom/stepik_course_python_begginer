a = int(input())
b = int(input())

num = a
max_sum = 0
for i in range(a, b + 1):
    total = 0
    for j in range(2, i // 2 + 1):
        if i % j == 0:
            total += j
    total += 1 + i
    if total >= max_sum:
        max_sum = total
        num = i
print(num, max_sum)
