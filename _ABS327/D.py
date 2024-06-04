N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

from collections import defaultdict, deque


def bfs(loot):
    s = deque()
    s.append(loot)
    visited = [0] * (len(g.keys()) + 1)
    visited[loot] = 1
    while s:
        node = s.popleft()
        for next_node in g[node]:
            if visited[next_node] == visited[node]:
                print('No')
                exit()
            if visited[next_node] == 0:
                s.append(next_node)
                visited[next_node] = visited[node] * -1


g = defaultdict(set)
for a, b in zip(A, B):
    g[a].add(b)
    g[b].add(a)

bfs(1)
print('Yes')
