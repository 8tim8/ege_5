for a in range(100):
    f = True
    for x in range(1, 100):
        for y in range(1, 100):
            if ((x**2 + y**2 < a) or (x > 3) or (y >= 5)) == 0:
                f = False
                break
    if f:
        print(a)
        break
