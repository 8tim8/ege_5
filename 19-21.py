from functools import lru_cache

@lru_cache(None)
def f(x, kol_xod, max_):
    if x >= 41:
        return kol_xod % 2 == max_ % 2
    if kol_xod == max_:
        return False

    p1 = f(x + 1, kol_xod + 1, max_)
    p2 = f(x + 2, kol_xod + 1, max_)
    p3 = f(x * 2, kol_xod + 1, max_)

    if x <= 25:
        if kol_xod % 2 != max_ % 2:
            return p1 or p2 or p3
        else:
            return p1 and p2 and p3
    else:
        if kol_xod % 2 != max_ % 2:
            return p1 or p2
        else:
            return p1 and p2


# for s in range(1, 40 + 1):
#     for j in range(1, 1000000):
#         if f(s, 0, j):
#             if j == 4:
#                 print(s, j)
#             if j == 6:
#                 print(s, j)
#             break

for s in range(1, 40 + 1):
    for j in range(1, 1000000):
        if f(s, 0, j):
            if j == 3:
                if (f(s + 1, 1, 3) + f(s + 2, 1, 3) + f(s * 2, 1, 3)) == 2:
                    print(s)
            break

