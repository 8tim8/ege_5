s = 2**29 * 3
print(s)
s //= 3
n, k = 0, 1
while s > k:
    s -= k
    k *= 2
    n += 1
print(n)
