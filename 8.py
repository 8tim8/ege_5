from itertools import *

s = 'НИКОЛАЙ'
k = 0
comb = product(s, repeat=11)
for i in comb:
    s = ''.join(i)
    if s[0] != 'Й' and s.count('О') == 1 and s.count('И') == 1 and s.count('А') == 1:
        k += 1
print(k)
