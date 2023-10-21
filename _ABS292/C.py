N = int(input())
ct = 0
dp1 = dict()
dp2 = dict()
x = 0
y = 0
EF = []
for e in range(1, int(N / 2) + 1):
    EF.append([e, N - e])
for e, f in EF:
    AB = e
    CD = f
    AB_ = 0
    CD_ = 0
    if e in dp1:
        AB_ = dp1[e]
        x += 1
    else:
        for a in range(1, e + 1):
            if e % a == 0:
                AB_ += 1
        dp1[e] = AB_
        y += 1
    if f in dp1:
        CD_ = dp1[f]
        x += 1
    else:
        for c in range(1, f + 1):
            if f % c == 0:
                CD_ += 1
        dp1[f] = CD_
        y += 1
    if e == f:
        ct += AB_ * CD_
    else:
        ct += AB_ * CD_ * 2



print(ct, x, y)