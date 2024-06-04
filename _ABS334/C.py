N, K = map(int, input().split())
A = list(map(int, input().split()))
dp = [0] * K
if len(A) == 1:
    print('0')
else:
    for i, a in enumerate(A):
        if i == 0:
            continue
        elif i == 1:
            dp[i] = abs(A[1] - A[0])
        elif i % 2 == 0:
            dp[i] = min(dp[i - 1], dp[i - 2] + abs(A[i - 1] - A[i]))
        else:
            dp[i] = dp[i - 1] + abs(A[i - 1] - A[i])
print(dp[-1])