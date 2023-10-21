N, K, P = map(int, input().split())
C, A = [], []
T = [float("inf") for _ in range(N + 1)]
for _ in range(N):
    tmp = list(map(int, input().split()))
    C.append(int(tmp[0]))
    A.append(tmp[1:])
print(A)

for i in range(len(T + 1)):
    if T[i - 1] == float('inf') and sum(T[:i]) >= P:
        T[i] = sum([T[:i]])
    else:
        