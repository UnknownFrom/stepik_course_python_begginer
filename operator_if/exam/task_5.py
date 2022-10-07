num = int(input())

if num % 2 == 1 or (num % 2 == 0 and 6 <= num <= 20):
    print('YES')
else:
    print('NO')
