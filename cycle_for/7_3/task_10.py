n = int(input())

largest_1 = 0
largest_2 = 0

for i in range(n):
    num = int(input())
    if largest_2 < num:
        largest_2 = num
        if largest_1 < largest_2:
            largest_1, largest_2 = largest_2, largest_1
print(largest_1)
print(largest_2)
