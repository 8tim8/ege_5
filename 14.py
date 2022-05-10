a = 15 * 1728**8 + 9 * 144**12 + 7 * 12**12 + 154
b = ''
while a > 0:
    if a % 12 > 9:
        b = 'A' + b
    else:
        b = str(a % 12) + b
    a //= 12
print(b.count('0'))
