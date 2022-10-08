num = int(input())

dig = num % 10

is_same = True

while num != 0 and is_same:
    if num % 10 != dig:
        is_same = False
    num //= 10
if is_same:
    print('YES')
else:
    print('NO')
