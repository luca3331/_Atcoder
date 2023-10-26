from collections import defaultdict

N = int(input())
G = defaultdict(list)
for i in range(N - 1):
    AB = list(map(int, input().split()))
    G[AB[0]].append(AB[1])
    G[AB[1]].append(AB[0])
print(G)
max_len, maxLenRoute = 0, []

def dfs(seen, curNode, Route):
    Route.append(curNode)
    global max_len, maxLenRoute
    if len(seen) > max_len:
        maxLenRoute = Route[:]
        max_len = len(Route)
    nextNodes = G.get(curNode)
    if nextNodes is None:
        return seen[:-1], None, Route[:-1]
    for node in nextNodes:
        if not node in seen:
            seen.append(node)
            seen, _, Route = dfs(seen, node, Route)
    return seen, Route[-1], Route[:-1]


_, u, Route1 = dfs([1], 1, [])
_, v, Route2 = dfs([u], u, [])
print(len(Route1) + 1 - len(Route2) + 1 + 1)
