for n in range(1, 100000):

    b = bin(n)[2:]
    q = n
    b += str(sum(int(x) for x in list(str(q))) % 2)
    q = int(b, 2)
    b += str(sum(int(x) for x in list(str(q))) % 2)
    q = int(b, 2)
    b += str(sum(int(x) for x in list(str(q))) % 2)
    if int(b, 2) > 1028:
        print(int(b, 2))
        break

# 1035
