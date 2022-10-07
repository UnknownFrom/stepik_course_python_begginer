num = int(input())

if 36 < num or num < 0:
    print('ошибка ввода')
elif num == 0:
    print('зеленый')
elif 1 <= num <= 10:
    if num % 2 == 0:
        print('черный')
    else:
        print('красный')
elif 11 <= num <= 18:
    if num % 2 == 0:
        print('красный')
    else:
        print('черный')
elif 19 <= num <= 28:
    if num % 2 == 0:
        print('черный')
    else:
        print('красный')
else:
    if num % 2 == 0:
        print('красный')
    else:
        print('черный')
