H, W = map(int, input().split())
S = [input() for _ in range(H)]
coo = []
new_coo = []
for i in range(H):
    for j in range(W):
        if S[i][j] == '#':
            coo.append((i, j))

def search(visited, h, w):
    for x in [-1, 0, 1]:
        for y in [-1, 0, 1]:
            new_y, new_x = h + x, w + y
            if 0 <= new_y < H and 0 <= new_x < W:
                if S[new_y][new_x] == '#':
                    if (new_y, new_x) not in visited:
                        visited.append((new_y, new_x))
                        search(visited, new_y, new_x)

ct = 0
while len(coo):
    ct += 1
    visited = []
    h, w = coo[0][0], coo[0][1]
    search(visited, h, w)
    for coo_ in visited:
        coo.remove(coo_)

print(ct)