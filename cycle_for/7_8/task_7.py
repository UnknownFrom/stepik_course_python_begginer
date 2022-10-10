for n in range(11):
    for k in range(21):
        for m in range(201):
            if n + k + m == 100 and 10 * n + 5 * k + 0.5 * m == 100:
                print(f'Быков = {n}')
                print(f'Коров = {k}')
                print(f'Телят = {m}')
                print()
