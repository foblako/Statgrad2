f = open("09.csv")
c = 0
s = []
for i in range(6400):
    s.append(f.readline().strip().split(";"))
s[0][0] = s[0][0][3:]
k = 0
for st in s:
    ch = [int(x) for x in st if int(x) % 2 == 0]
    nch = [int(x) for x in st if int(x) % 2 != 0]
    if sum(ch) > sum(nch) and len(nch) > len(ch) and len(st) == len(set(st)):
        k += 1
print(k)

# 303
