f = open("27-b.txt")
n = int(f.readline())

k = 0
m = [[0] * 9 for i in range(4)]

for i in range(n):
    x = int(f.readline())
    ost = x % 4
    k3 = 0
    while x % 3 == 0:
        k3 += 1
        x //= 3
    if k3 > 8: k3 = 8

    for h in range(8 - k3, 9):
        k += m[(4 - ost) % 4][h]

    m[ost][k3] += 1
print(k)
# 306 360950279
