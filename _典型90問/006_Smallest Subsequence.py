N, K = list(map(int, input().split()))
S = input()
char_list = set(S)
nex = [[-1 for _ in range(N)] for _ in range(27)]

res = [[N] * 26 for _ in range(N + 1)]

for i in range(N - 1, -1, -1):
    # i + 1 文字目以降の結果を一旦 i 文字にコピー
    for j in range(26):
        res[i][j] = res[i + 1][j]

    # i 文字目の情報を反映させる
    res[i][ord(S[i]) - ord('a')] = i

print(res)