NSML = input().split()
N, SML = int(NSML[0]), NSML[1:]
eggs = sorted([(6, int(SML[0])), (8, int(SML[1])), (12, int(SML[2]))], key= lambda x:x[1])
dp = [float('inf')] * (10 ** 4)
yasui_egg = eggs[0]
size = [6, 8, 12]
for i in range(yasui_egg[0] + 1):
    dp[i] = yasui_egg[1]
for n in range(yasui_egg[0] + 1, N + 1):
    for egg in eggs: #安い順
        if n <= eggs[1][0]:
            dp[n] = eggs[1][1]
        elif n <= eggs[2][0]:
            dp[n] = min(dp[n], eggs[2][1])
        dp[n] = min(dp[n], dp[n-egg[0]] + egg[1])
print(dp[N])
