for x in range(37):
    a = 5 * 37 ** 3 + (2 + x) * 37 ** 2 + 8 * 37 ** 1 + (x + 9)
    if a % 36 == 0:
        print(a // 36)
        break

# 7348
