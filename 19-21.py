def f(a, b, c, m):
    if (a + b) >= 81: return (c % 2) == (m % 2)
    if c == m: return 0
    if a > b:
        h = [f(a, b * 2, c + 1, m), f(a, b + 2, c + 1, m),
             f(a, b + 1, c + 1, m)]
    else:
        h = [f(a + 1, b, c + 1, m), f(a + 2, b, c + 1, m), f(a * 2, b, c + 1, m)]
    return any(h) if (c + 1) % 2 == m % 2 else all(h)


for b in range(1, 69):
    for m in range(1, 5):
        if f(12, b, 0, m):
            print(b, m)
            break

# 55
# 31 54
# 50
