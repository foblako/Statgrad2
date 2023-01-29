def f(x, y, k1, k2):
    if x == y: return 1
    if x > y: return 0
    if x < y:
        if k1 == k2 == "+1":
            return f(x * 2, y, "*2", k2)
        elif k1 == k2 == "*2":
            return f(x + 1, y, "+1", k2)
        else:
            return f(x * 2, y, "*2", k1) + f(x + 1, y, "+1", k1)


print(f(1, 14, '', ''))

# 6
