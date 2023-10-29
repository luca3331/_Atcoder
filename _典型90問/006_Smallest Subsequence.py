N, K = list(map(int, input().split()))
S = input()
nex = [[N] * 26 for _ in range(N + 1)]


for i in range(N - 1, -1, -1):
    # i + 1 文字目以降の結果を一旦 i 文字にコピー
    for j in range(26):
        nex[i][j] = nex[i+1][j]
    nex[i][ord(S[i]) - ord('a')] = i


ans = ""
now = 0
for i in range(K):
    for c in range(26):
        if N - nex[now][c] >= K - i:
            ans += chr(ord('a') + c)
            now = nex[now][c] + 1
            break
print(ans)



# for i in range(K):
#     for c in range(26):
#         if nex[i][c] <= N - (K - i):
#             ans += chr(ord('a') + c)
#             now = nex[now][c] + 1
