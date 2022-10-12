for a in range(1, 151):
    for b in range(a, 151):
        for c in range(b, 151):
            for d in range(c, 151):
                num = a ** 5 + b ** 5 + c ** 5 + d ** 5
                for e in range(1, 151):
                    if num < e ** 5:
                        break
                    elif num == e ** 5:
                        print(a + b + c + d + e)
