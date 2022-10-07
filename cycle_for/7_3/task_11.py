is_all_even = True

for i in range(10):
    num = int(input())
    if num % 2 != 0:
        is_all_even = False
if is_all_even:
    print('YES')
else:
    print('NO')
