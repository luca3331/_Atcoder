N = int(input())
S = list(input())
T = 'atcoder'
# T = 'atc'

dp = [[0] * (len(T) + 1) for _ in range(len(S) + 1)]
dp[0][0] = 1

for j in range(len(T) + 1):
    for i in range(1, len(S) + 1):
        if S[i - 1] == T[j - 1]:
            dp[i][j] += (dp[i - 1][j - 1] + dp[i - 1][j]) % (10**9 + 7)
        else:
            dp[i][j] += (dp[i - 1][j]) % (10**9 + 7)

print(dp[-1][-1])