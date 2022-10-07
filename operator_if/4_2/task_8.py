column_1 = int(input())
row_1 = int(input())
column_2 = int(input())
row_2 = int(input())

if -1 <= (column_1 - column_2) <= 1 and -1 <= (row_1 - row_2) <= 1:
    print('YES')
else:
    print('NO')
