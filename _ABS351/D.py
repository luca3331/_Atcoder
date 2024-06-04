from collections import deque
import numpy as np
H, W = input().split()
S = [list(input()) for _ in range(int(H))]
SS = np.array(S)
indices = np.where(SS == '#')
magnet = set()
taboo = set()
for row, col in zip(indices[0], indices[1]):
    magnet.add((row, col))
    for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:  # 上下左右の移動
        nr, nc = row + dr, col + dc
        if 0 <= nr < int(H) and 0 <= nc < int(W):
            taboo.add((nr, nc))

# def bfs(start):
#     queue = deque([[start]])
#     while queue:
#         current = queue.popleft()
#
#         for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:  # 上下左右の移動
#             nr, nc = current[0] + dr, current[1] + dc
#             if 0 <= nr < int(H) and 0 <= nc < int(W) and not visited[nr][nc] and matrix[nr][nc] != 'X':
#                 queue.append((nr, nc))
#                 visited[nr][nc] = True
#
def dfs(row, col, visited, island):
    if row < 0 or col < 0 or row >= int(H) or col >= int(W) or (row, col) in magnet or visited[row][col]:
        return 0
    if (row, col) in taboo:
        island.append((row, col))
        return 1

    visited[row][col] = True
    island.append((row, col))
    size = 1

    for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        size += dfs(row + dr, col + dc, visited, island)

    return size


def find_islands(taboo):
    rows, cols = int(H), int(W)
    visited = [[False] * cols for _ in range(rows)]
    islands = []

    for row in range(rows):
        for col in range(cols):
            if (row, col) not in taboo and not visited[row][col]:
                island = []
                size = dfs(row, col, visited, island)
                if len(island):
                    islands.append((island, size))

    return islands


islands = find_islands(taboo)
sorted_islands = sorted(islands, key=lambda x: x[0])
if len(sorted_islands) == 0:
    print(1)
else:
    print(len(set(sorted_islands[0][0])))

# for island, size in islands:
#     print(f"島の要素数: {size}, 島の座標: {island}")
#
# print(taboo)
# print(magnet)
