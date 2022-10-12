a = int(input())
b = int(input())

total = 0
for i in range(a, b + 1):
    counter = 0
    for j in range(2, i // 2 + 1):
        if i % j == 0:
            counter += 1
    if counter == 0 and i != 1:
        print(i)
