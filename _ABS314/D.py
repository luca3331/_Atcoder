H, W = map(int, input().split())
C = [input() for _ in range(H)]
row = [[0] * 5 for _ in range(H)]
col = [[0] * 5 for _ in range(W)]

for h in range(H):
    for w in range(W):
        x = ord(C[h][w]) - ord('a')
        row[h][x] += 1
        col[w][x] += 1

print(col, row)

hh, ww = H, W
for c in col:
    if hh in c:
        row[c.index(hh)][x] -= 1
for r in row:
    if ww in r:
        col[r.index(ww)][x] -= 1


print(col, row)