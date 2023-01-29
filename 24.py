s = open("24.txt").readline()
s = s.split("F")[1:-1]
m = 0
l = "F"
for i in range(len(s)):
    if s[i].count("A") <= 2:
        l += s[i] + "F"
        m = max(m, len(l))
    else:
        l = "F"
print(m)

# 266
