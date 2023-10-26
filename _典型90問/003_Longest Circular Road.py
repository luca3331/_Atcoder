from collections import defaultdict, deque

N = int(input())
G = defaultdict(list)
for i in range(N - 1):
    AB = list(map(int, input().split()))
    G[AB[0]].append(AB[1])
    G[AB[1]].append(AB[0])
# print(G)

def dfs(startNode):
    dist = [0 for _ in range(N + 1)]
    q = deque([startNode])
    seen = set()
    while len(q):
        cur_node = q.popleft()
        seen.add(cur_node)
        for node in G.get(cur_node):
            if node in seen:
                continue
            else:
                q.append(node)
                dist[node] = dist[cur_node] + 1
    return dist

dist1 = dfs(1)
u = dist1.index(max(dist1))
dist2 = dfs(u)
v = dist2.index(max(dist2))
print(dist2[v] + 1)
