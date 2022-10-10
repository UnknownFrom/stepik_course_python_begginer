for e in range(150):
    for a in range(e):
        for b in range(e-a):
            for c in range(e-b):
                for d in range(e-c):
                    if a**5 + b**5 + c**5 + d**5 == e**5:
                        print(a+b+c+d+e)
