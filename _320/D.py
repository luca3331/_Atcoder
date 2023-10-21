from collections import defaultdict, deque
N, M = list(map(int, input().split()))
d = defaultdict(list)
A, B, X, Y = [], [], [], []
for n in range(M):
    a, b, x, y = list(map(int, input().split()))
    d[a].append((b, x, y))
    d[b].append((a, -x, -y))

def bfs():
    seen = []
    seeen = []
    q = deque([1])
    p_x, p_y = 0, 0
    while q:
        dest = q.popleft()
        for v in d[dest]:
            if not v[0] in seen:
                p_x += v[1]
                p_y += v[2]
                seen.append(v[0])
                q.append(v[0], p_x, p_y)
                p_x -= v[1]
                p_y -= v[2]
    print(seen)

bfs()
