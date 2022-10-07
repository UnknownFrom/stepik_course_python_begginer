n = int(input())

num_1 = 1
num_2 = 1

if n == 1:
    print(1)
elif n == 2:
    print(1, 1)
else:
    print(1, 1, end=' ')
    for i in range(3, n + 1):
        num_3 = num_1 + num_2
        print(num_3, end=' ')
        num_1, num_2 = num_2, num_3
