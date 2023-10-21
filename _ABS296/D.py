N, M = map(int, input())



for a in range(1, N):
    for b in range(1, N):
        if a * b == M:
            print('Yes')

for x in range(M, N * N):
    x %