from collections import defaultdict, deque

N, M = map(int, input().split())
# G = defaultdict(list)
G = [[-1 for _ in range(N + 1)] for _ in range(N + 1)]
q = deque()
memo = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
for _ in range(N):
    tmp = list(map(int, input().split()))
    G[tmp[0]][tmp[1]] = tmp[2]
    G[tmp[1]][tmp[0]] = tmp[2]
print(G)


def dfs(start, node, seen):
    neighbors = []
    for i in range(len(G[node])):
        if not G[node][i] == -1:
            neighbors.append([i, G[node][i]])
    for neighbor in neighbors:
        if not neighbor[0] in seen:
            q.append(neighbor[0])
        if start != node and memo[start][node] == 0:
            memo[start][node] = neighbor[1]
    while q:
        next_node = q.pop()
        seen.add(next_node)
        dfs(start, next_node, seen)


for key in G.keys():
    seen = set()
    dfs(key, key, seen)

print(memo)
