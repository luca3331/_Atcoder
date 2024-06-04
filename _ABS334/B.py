A, M, L, R = map(int, input().split())
if L < A:
    AA = L
    while True:
        if (L - AA) // M == 0:
            break
        else:
            AA += 1
    print((R - AA) // M + 1)

else:
    AA = A
    while AA < L:
        AA += M
    print((R - AA) // M + 1)
