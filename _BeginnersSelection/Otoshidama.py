N, Y = map(int, input().split())
flag = False
for x in range(N + 1):
    for y in range(N - x + 1):
        z = N - x - y
        if z >= 0 and x + y + z == N and 10000 * x + 5000 * y + 1000 * z == Y:
            print("{} {} {}".format(x, y, z))
            flag = True
            break
        if flag:
            break
    if flag:
        break
if not flag:
    print("-1 -1 -1")
