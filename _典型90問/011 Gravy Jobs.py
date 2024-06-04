N = int(input())
DCS = []
for i in range(N):
    DCS.append(list(map(int, input().split())))

DCS.sort(key=lambda x: x[0])
dp = [[0] * (DCS[-1][0] + 1) for _ in range(N + 1)]

for j in range(1, DCS[-1][0] + 1):
    for i in range(1, N + 1):
        if DCS[i-1][0] <= j:
            day_before = max(0, j - DCS[i-1][1])
            dp[i][j] = max(dp[i-1][day_before] + DCS[i-1][2], max(dp[i-1][j], dp[i][j-1]))
        else:
            dp[i][j] = dp[i][j-1]
print(dp)
# for i in range(N, 0, -1):
