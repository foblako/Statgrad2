def f(x, y, w, z):
    return (x == (not y)) <= ((z <= (not w)) and (x <= y))


for x in range(2):
    for y in range(2):
        for w in range(2):
            for z in range(2):
                print(y, w, z, x, f(x, y, w, z))

# ywzx
