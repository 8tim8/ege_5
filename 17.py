f = open('17.txt')
a = [int(x) for x in f]
s = 0
k = 0
m = 0
kolvo = 0
for i in a:
    if i % 2 == 1:
        k += 1
        s += i
sr = s / k
for i in range(2, len(a)):
    x = a[i - 2]
    y = a[i - 1]
    z = a[i]
    x1 = x % 3
    y1 = y % 3
    z1 = z % 3
    if x1 != y1 and y1 != z1 and x1 != z1:
        if (x < sr and y >= sr and z >= sr) or (z < sr and y >= sr and x >= sr) or (y < sr and x >= sr and z >= sr):
            kolvo += 1
            m = max(x+y+z, m)
print(kolvo, m)
