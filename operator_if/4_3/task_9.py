a1, b1 = int(input()), int(input())
a2, b2 = int(input()), int(input())

if b2 < a1 or b1 < a2:
    print('пустое множество')
elif a2 <= a1 and b2 == a1:
    print(b2)
elif a2 == b1 and b2 >= b1:
    print(a2)
elif a1 <= a2:
    if b2 <= b1:
        print(a2, b2)
    else:
        print(a2, b1)
elif a2 <= a1:
    if b1 <= b2:
        print(a1, b1)
    else:
        print(a1, b2)
