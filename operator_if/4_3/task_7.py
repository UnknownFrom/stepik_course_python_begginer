color_1 = input()
color_2 = input()

if color_1 == color_2 and color_1 in ['красный', 'синий', 'желтый']:
    print(color_1)
elif color_1 == 'красный' and color_2 == 'желтый' or color_2 == 'красный' and color_1 == 'желтый':
    print('оранжевый')
elif color_1 == 'красный' and color_2 == 'синий' or color_2 == 'красный' and color_1 == 'синий':
    print('фиолетовый')
elif color_1 == 'синий' and color_2 == 'желтый' or color_2 == 'синий' and color_1 == 'желтый':
    print('зеленый')
else:
    print('ошибка цвета')
