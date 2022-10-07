num = int(input())
dig_1 = num // 1000
dig_2 = num % 1000 // 100
dig_3 = num % 100 // 10
dig_4 = num % 10

if dig_1 + dig_4 == dig_2 - dig_3:
    print('ДА')
else:
    print('НЕТ')