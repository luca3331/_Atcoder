N, Q = input().split()
S = input()
T = [0] * (int(N) + 1)
LR = [list(map(int, input().split())) for _ in range(int(Q))]
for n in range(int(N) - 1):
    if n == 0 and S[n] == S[n+1]:
        T[n] = 1
    T[n + 1] += T[n]
    if S[n] == S[n + 1]:
        T[n + 1] += 1
# print(T)
for lr in LR:
    print(T[lr[1]-1] - T[lr[0]-1])