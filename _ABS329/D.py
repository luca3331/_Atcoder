import itertools
N = int(input())
T = []
S = []
TT = [[0] * N for _ in range(N)]
for n in range(N):
    tmp = list(input())
    tmpp = []
    for j in range(N):
        if tmp[j] == 'o':
            tmpp.append(j)
    T.append(tmpp)
    S.append(tmp)
for i in range(N):
    for j in range(N):
        TT[i][j] = sum([1 for x in range(i + 1, N) if S[x][j] == 'o'])
print(S)
print(T)
print(TT)
ct = 0
for i in range(N):
    for v1v2 in itertools.combinations(T[i], 2):
        v1, v2 = v1v2[0], v1v2[1]
        ct += TT[i][v1] + TT[i][v2]
print(ct)