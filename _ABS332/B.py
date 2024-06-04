K, G, M = map(int, input().split())
Gv, Mv = 0, 0
for ki in range(K):
    if Gv == G:
        Gv = 0
    elif Mv == 0:
        Mv = M
    else:
        Gv = min(G, Gv + Mv)
        Mv = Mv - Gv
print(Gv, Mv)