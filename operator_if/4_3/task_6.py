num_1, num_2, operation = int(input()), int(input()), input()

if operation == '+':
    print(num_1 + num_2)
elif operation == '-':
    print(num_1 - num_2)
elif operation == '*':
    print(num_1 * num_2)
elif operation == '/':
    if num_2 == 0:
        print('На ноль делить нельзя!')
    else:
        print(num_1/num_2)
else:
    print('Неверная операция')
