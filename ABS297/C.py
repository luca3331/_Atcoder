H, W = map(int, input().split())
S = []
ct = 0
for _ in range(H):
    tmp = list(input())
    combo = 0
    s = []
    for t in range(len(tmp)):
        if tmp[t] == 'T':
            if t == len(tmp) - 1:
                s.append('T')
                continue
            combo += 1
            if combo == 2:
                s.append('P')
                s.append('C')
                ct += 1
                combo = 0
        elif tmp[t] != 'T' and combo == 1:
            s.append('T')
            s.append('.')
            combo = 0
        else:
            s.append('.')
    S.append(s)
for s in S:
    print(*s, sep='')
