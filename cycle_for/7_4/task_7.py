num = int(input())
counter = 0
while num != 0:
    if num - 25 >= 0:
        num -= 25
        counter += 1
    elif num - 10 >= 0:
        num -= 10
        counter += 1
    elif num - 5 >= 0:
        num -= 5
        counter += 1
    elif num - 1 >= 0:
        num -= 1
        counter += 1
print(counter)
