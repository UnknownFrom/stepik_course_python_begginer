month = int(input())

if month == 2:
    print(28)
elif month % 2 == 0 and month <= 7 or month % 2 == 1 and 8 <= month <= 12:
    print(30)
else:
    print(31)
