N = int(input())
WX = [input().split() for _ in range(N)]


max_ct = 0
for i in range(24 + 1): #i時からi+1時まで会議
    ct = 0
    for wx in WX:
        w, x = map(int, wx)
        startTime = i + x
        endTime = i + 1 + x
        if 9 <= startTime % 24 and startTime % 24 <= 18 and 9 <= endTime % 24 and endTime % 24 <= 18:
            ct += w
    if max_ct < ct:
        max_ct = ct
print(max_ct)