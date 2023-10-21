R, C = map(int, input().split())
B = []
vector = [[-1, 0], [0, -1], [1, 0], [0, 1]]
for i in range(R):
    tmp = list(input())
    for j in range(C):
        if tmp[j].isdigit():
            tmp[j] = int(tmp[j])
        else:
            tmp[j] = tmp[j]
    B.append(tmp)

# for i in range(R):
#     for j in range(C):
#         if str(B[i][j]).isdigit():
#             s = B[i][j]
#             B[i][j] = '.'
#             for m in range(R):
#                 for n in range(C):
#                     if abs(i - m) + abs(j - n) <= s and not str(B[m][n]).isdigit():
#                         B[m][n] = '.'
# 数字のみを含む要素の位置を取得する
digit_positions = [(i, j) for i in range(R) for j in range(C) if str(B[i][j]).isdigit()]

# 各数字の要素に対して範囲内の要素を更新する
for i, j in digit_positions:
    s = B[i][j]
    B[i][j] = '.'

    # 範囲を制限する
    min_i = max(0, i - s)
    max_i = min(R - 1, i + s)
    min_j = max(0, j - s)
    max_j = min(C - 1, j + s)

    for m in range(min_i, max_i + 1):
        for n in range(min_j, max_j + 1):
            # 数字でない要素のみを更新する
            if not str(B[m][n]).isdigit() and abs(i - m) + abs(j - n) <= s:
                B[m][n] = '.'

for i in range(R):
    tmp = ""
    for j in range(C):
        tmp += B[i][j]
    print(tmp)