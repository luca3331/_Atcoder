H, W = map(int, input().split())
S = []
for _ in range(H):
    s = list(input())
    for w in range(W - 1):
        if s[w] == 'T' and s[w + 1] == 'T':
            s[w] = 'P'
            s[w + 1] = 'C'
    S.append(s)
for s in S:
    print(*s, sep='')

