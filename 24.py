f = open('24.txt')
s = f.readline()
s = 'A' + s + 'A'
poz = []
for i in range(len(s)):
    if s[i] in 'AB':
        poz.append(i)
otv = -1
for i in range(4, len(poz)):
    if poz[i] - poz[i - 4] > otv:
        otv = poz[i] - poz[i - 4] - 1
print(otv)

