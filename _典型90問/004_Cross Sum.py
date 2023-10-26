H, W = map(int, input().split())
A = [input().split() for _ in range(H)]
T_h = [0 for _ in range(H)]
T_w = [0 for _ in range(W)]

for h in range(H):
    AA = list(map(int, A[h]))
    T_h[h] = sum(AA)
for w in range(W):
    score = 0
    for h in range(H):
        score += int(A[h][w])
    T_w[w] = score
for h in range(H):
    for w in range(W):
        print(T_h[h] + T_w[w] - int(A[h][w]), "", end="")
    print("")