num = int(input())

dig = num % 10

is_ordered = True

while num != 0 and is_ordered:
    if num % 10 < dig:
        is_ordered = False
    dig = num % 10
    num //= 10
if is_ordered:
    print('YES')
else:
    print('NO')
