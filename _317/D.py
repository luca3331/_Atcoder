N = int(input())
X, Y, Z = [], [], []
X_Z, Y_Z = 0, 0  # それぞれの議席数
dp_z = []
changed_people = 0
for _ in range(N):
    x, y, z = map(int, input().split())
    X.append(x)
    Y.append(y)
    Z.append(z)
    if x < y:
        Y_Z += z
    else:
        X_Z += z
    if y - x > 0:
        dp_z.append([int(((x + y) / 2) + 1 - x), z])

majority_num = int(sum(Z) / 2 + 1)
dp = [[float('inf') for _ in range(len(dp_z))] for _ in range(majority_num - X_Z + 1)]
pass
if X_Z > Y_Z:
    print('0')
else:
    dp_z = sorted(dp_z, key=lambda n: n[1])
    w = []
    v = []
    for dpz in dp_z:
        w.append(dpz[0])
        v.append(dpz[1])

    for i in range(majority_num - X_Z + 1):
        for j in range(len(dp_z)):
            if i <= v[j]:
                dp[i][j] = min(dp[i][j - 1], w[j])
            else:
                if j - 1 < 0:
                    dp[i][j] = dp[i][j - 1]
                else:
                    dp[i][j] = min(dp[i - v[j]][j - 1] + w[j], dp[i][j - 1])

    print(dp[majority_num - X_Z][len(dp_z) - 1])

