a = [int(x) for x in open("17.txt")]
m5 = min(x for x in a if x % 10 == 5)
pairs = [a[i] ** 2 + a[i + 1] ** 2 for i in range(len(a) - 1) if
         min(a[i], a[i + 1]) % 10 == 5 and a[i] ** 2 + a[i + 1] ** 2 < m5 ** 2]
print(len(pairs), max(pairs))

# 403 99805561
