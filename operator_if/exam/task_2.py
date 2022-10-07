column_1, row_1 = int(input()), int(input())
column_2, row_2 = int(input()), int(input())

if (column_1 + row_1) % 2 == (column_2 + row_2) % 2:
    print('YES')
else:
    print('NO')
