N, S, K = map(int, input().split())
ans = 0
for ni in range(N):
    P, Q = map(int, input().split())
    ans += P * Q
if ans < S:
    print(ans + K)
else:
    print(ans)