import math
import bisect
N = int(input())
XY = [list(map(int, input().split())) for _ in range(N)]

max_arg = 0
# for xy in XY:
#     B_x, B_y = xy
#     XY_ = XY[:]
#     XY_.remove(xy)
#     # new_XY = sorted([((math.atan2(y - B_y, x - B_x) * 180 / math.pi + 360) % 360) for i, (x, y) in enumerate(XY_)])
#     new_XY = sorted([(360 + math.atan2(y - B_y, x - B_x) * 180 / math.pi) % 360 for i, (x, y) in enumerate(XY_)])
#     for nxy in XY_:
#         argA = (360 + math.atan2(nxy[1], nxy[0]) * 180 / math.pi) % 360
#         opposite = bisect.bisect_left(new_XY, (argA + 180) % 360)
#         print(opposite)
#         if max_arg < min(abs(new_XY[opposite] - argA), 360 - abs(new_XY[opposite] - argA)):
#             max_arg = min(abs(new_XY[opposite] - argA), 360 - abs(new_XY[opposite] - argA))
#     print(argA, opposite, new_XY)
# print(max_arg)

for xy in XY:
    XY_ = XY[:]
    XY_.remove(xy)
    sorted_arg = sorted([(360 + math.atan2(y - xy[1], x - xy[0]) * 180 / math.pi) % 360 for i, (x, y) in enumerate(XY_)])
    for arg in sorted_arg:
        opposite = bisect.bisect_left(sorted_arg, (arg + 180) % 360)
        if max_arg < min(abs(sorted_arg[min(opposite, len(sorted_arg) - 1)] - arg), 360 - abs(sorted_arg[min(opposite, len(sorted_arg) - 1)] - arg)):
            max_arg = min(abs(sorted_arg[min(opposite, len(sorted_arg) - 1)] - arg), 360 - abs(sorted_arg[min(opposite, len(sorted_arg)) - 1] - arg))
    # print(sorted_arg)
print(max_arg)