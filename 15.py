def f(x, y):
    return ((144 % x == 0) <= (x % y != 0)) or (x + y > 100) or (a - x > y)


for a in range(10000):
    if all(f(x, y) for x in range(1, 1000) for y in range(1, 1000)):
        print(a)
        break

# 97
