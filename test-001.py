n = 10
s = 0
for i in range(1, n+1):
    print(i)
    p = n - i
    s += (10**p) * i
print(s)
