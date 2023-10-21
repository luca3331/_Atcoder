H, W = map(int, input().split())
C = [input() for _ in range(H)]

def judge(a, b):
    value = 0
    for d in range(min(H, W)):
        if 0 <= a + d < h and 0 <= a - d < h and 0 <= b + d < w and 0 <= b - d < w:
            if C[a][b] != '#':
                return d - 1
            if C[a + d][b + d] != '#':
                return d - 1
            if C[a + d][b - d] != '#':
                return d - 1
            if C[a - d][b + d] != '#':
                return d - 1
            if C[a - d][b - d] != '#':
                return d - 1
        value = d
    return value


arr = []
for h in range(H):
    for w in range(W):
        value = judge(h, w)
        if value == 0:
            continue
        else:
            arr.append(value)

print(arr)