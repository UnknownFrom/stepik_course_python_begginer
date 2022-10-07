str_1 = input()
str_2 = input()
str_3 = input()

max_len = max(len(str_1), len(str_2), len(str_3))
min_len = min(len(str_1), len(str_2), len(str_3))

d = (max_len - min_len) / 2

mid_len = min_len + d
if len(str_1) - mid_len == 0 or len(str_2) - mid_len == 0 or len(str_3) - mid_len == 0:
    print('YES')
else:
    print('NO')
