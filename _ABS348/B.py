N = int(input())
XY = []
for _ in range(N):
    XY.append(list(map(int, input().split())))
for xy in XY:
    x, y = xy[0], xy[1]
    max_dist = 0
    max_index = 0
    for i, xxyy in enumerate(XY):
        xx, yy = xxyy[0], xxyy[1]
        dist = ((x-xx)**2+(y-yy)**2)**(1/2)
        if max_dist < dist:
            max_dist = dist
            max_index = i + 1
    print(max_index)