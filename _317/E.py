H, W = map(int, input().split())
A = [list(input()) for _ in range(H)]
direction = {'>':[0, 1], 'v':[1, 0], '<':[0, -1], '^':[-1, 0]}
neighbors = [[0, 1], [1, 0], [0, -1], [-1, 0]]
seen = set()

def looked(char, r, c):
    r += direction[char][0]
    c += direction[char][1]
    while 0 <= r < H and 0 <= c < W and A[r][c] == '.':
        A[r][c] = '!'
        r += direction[char][0]
        c += direction[char][1]

for r in range(H):
    for c in range(W):
        if A[r][c] == 'S':
            start = r, c
        if A[r][c] in direction.keys():
            looked(A[r][c], r, c)

def dfs(r, c, ct):
    if r < 0 or r >= H or c < 0 or c >= W or A[r][c] == '#':
        return  # Out of bounds or hitting a wall
    if A[r][c] == 'G':
        return ct  # Reached the goal

    A[r][c] = '#'  # Mark as visited
    neighbors = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    for neighbor in neighbors:
        next_r = r + neighbor[0]
        next_c = c + neighbor[1]
        result = dfs(next_r, next_c, ct + 1)
        if result is not None:
            return result

    return None  # No path found

result = dfs(start[0], start[1], 0)
if result is None:
    print('-1')
else:
    print(result)
