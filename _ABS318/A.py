N, M, P = map(int, input().split())
if N < M:
    print('0')
else:
    print(int((N - M) / P) + 1)
