N = int(int(input()))
ct = 0
# X <= Yと仮定する
# Xを決めるとY = N - X
for X in range(1, N + 1):
    x, y = 0, 0
    Y = N - X
# A <= Bと仮定する
# Aを決めるとB = N / A
    for A in range(1, int(N**1/2) + 1):
        if X % A == 0:
            B = X / A
            if A == B:
                x = 1
            else:
                x = 2
        else:
            continue
        for C in range(1, int((N - X)**1/2) + 1):
            if Y % C == 0:
                D = Y / C
                if C == D:
                    y = 1
                else:
                    y = 2
                ct += x * y

print(ct)