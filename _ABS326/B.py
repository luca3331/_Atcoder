N = input()
for i in range(int(N), 920):

    x, y, z = map(int, list(str(i)))
    if z == x * y:
        print(i)
        break