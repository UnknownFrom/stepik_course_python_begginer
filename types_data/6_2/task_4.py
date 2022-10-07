name_1 = input()
name_2 = input()
name_3 = input()

max_len = max(len(name_1), len(name_2), len(name_3))
min_len = min(len(name_1), len(name_2), len(name_3))

if len(name_1) == min_len:
    print(name_1)
elif len(name_2) == min_len:
    print(name_2)
else:
    print(name_3)
if len(name_1) == max_len:
    print(name_1)
elif len(name_2) == max_len:
    print(name_2)
else:
    print(name_3)