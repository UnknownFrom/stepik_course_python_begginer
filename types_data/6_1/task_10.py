num = int(input())

dig_1 = num // 100
dig_2 = num // 10 % 10
dig_3 = num % 10

max_dig = max(dig_1, dig_2, dig_3)
min_dig = min(dig_1, dig_2, dig_3)
mid_dig = dig_1 + dig_2 + dig_3 - max_dig - min_dig

if max_dig - min_dig == mid_dig:
    print('Число интересное')
else:
    print('Число неинтересное')
