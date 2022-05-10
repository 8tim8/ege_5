for i in range(10, 1000):
    s = str(i)
    max_i = 0
    min_i = 10000
    for j in range(len(s) - 1):
        s1 = int(s[j] + s[j + 1])
        max_i = max(s1, max_i)
        min_i = min(s1, min_i)
    if max_i - min_i == 44:
        print(i)
        break
