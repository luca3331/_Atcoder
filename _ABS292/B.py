N, Q = map(int, input().split())
ev = [input().split() for _ in range(Q)]
C = dict()
for e in ev:
    if e[0] == '1':
        if e[1] in C:
            C[e[1]] += 1
        else:
            C[e[1]] = 1
    if e[0] == '2':
        C[e[1]] = 2
    if e[0] == '3':
        if e[1] in C and C[e[1]] == 2:
            print('Yes')
        else:
            print('No')
