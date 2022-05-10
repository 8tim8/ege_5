def f(n):
    if n == 0:
        return 0
    elif n % 3 != 0:
        return f(n - 1) + 1
    else:
        return f(n // 3)


def tr(n):
    s = 0
    while n > 0:
        s = n % 3 + s
        n //= 3
    return s


m = 0
for i in range(12 * 10**8, 16 * 10**8 + 1):
    m = max(m, tr(i))
print(m)
