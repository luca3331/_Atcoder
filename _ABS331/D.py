N, Q = map(int, input().split())
P = [list(input()) for _ in range(N)]
left_T = [[0] * N for _ in range(N)]
right_T = [[0] * N for _ in range(N)]

for i in range(N):
    for j in range(N):
        left_T[i][j] = P[i][j:N].count('B')
        right_T[i][j] = P[i][0:j+1].count('B')

for qq in range(Q):
    A, B, C, D = map(int, input().split())
