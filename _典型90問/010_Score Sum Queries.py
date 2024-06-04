from collections import deque
N = int(input())
T = [[0] * (N + 1) for _ in range(2)]
c1, c2 = deque(), deque()
for n in range(1, N + 1):
    c, p = map(int, input().split())
    if c == 1:
        T[0][n] = T[0][n - 1] + p
        T[1][n] = T[1][n - 1]
    if c == 2:
        T[1][n] = T[1][n - 1] + p
        T[0][n] = T[0][n - 1]
Q = int(input())
for q in range(Q):
    l, r = map(int, input().split())
    print(T[0][r] - T[0][l-1], T[1][r] - T[1][l-1])
