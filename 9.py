f = open('9.txt')
k = 0
for i in f:
    a = []
    x, y, z, w = i.split()
    a.append(int(x))
    a.append(int(y))
    a.append(int(z))
    a.append(int(w))
    a.sort()
    if (a[0] + a[3]) == (a[1] + a[2]) and (a[0] + a[3]) % 2 == 1:
        k += 1
print(k)
