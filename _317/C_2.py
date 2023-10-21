from collections import defaultdict, deque

N, M = map(int, input().split())
# G = defaultdict(list)
G = [[-1 for _ in range(N + 1)] for _ in range(N + 1)]
q = deque()
seen = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
memo = [[-1 for _ in range(N + 1)] for _ in range(N + 1)]
for _ in range(N):
    tmp = list(map(int, input().split()))
    G[tmp[0]][tmp[1]] = tmp[2]
    G[tmp[1]][tmp[0]] = tmp[2]
print(G)


def dfs(graph, start_node, visited=None):
    if visited is None:
        visited = set()

    # 開始ノードを訪問済みにマーク
    visited.add(start_node)

    # 開始ノードを表示または処理
    print(start_node)

    # 隣接行列から開始ノードに接続されているすべてのノードを取得
    adjacent_nodes = graph[start_node]

    for node, is_connected in enumerate(adjacent_nodes):
        # 未訪問の隣接ノードを再帰的に探索
        if is_connected and node not in visited:
            dfs(graph, node, visited)


# 隣接行列の例
adjacency_matrix = [
    [0, 1, 1, 0],
    [1, 0, 0, 1],
    [1, 0, 0, 0],
    [0, 1, 0, 0]
]

# ノード0からDFSを開始
start_node = 0
dfs(adjacency_matrix, start_node)

