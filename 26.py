f = open("26.txt")
cubes = []
for i in f:
    size, color = i.split()
    size = int(size)
    cubes.append([size, color])
cubes.sort(reverse=1)

sklad = []
while len(cubes) > 0:
    block = [cubes.pop(0)]
    for i in range(len(cubes)):
        if cubes[i][1] != block[-1][1] and block[-1][0] - cubes[i][0] >= 5:
            block.append(cubes[i])
            cubes[i] = ""
    cubes = [x for x in cubes if x != ""]
    sklad.append(block)
print(max(len(x) for x in sklad), len(sklad))
