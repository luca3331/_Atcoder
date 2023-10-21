A, B, C, X, Y = list(map(int, input().split()))
min_v = 10**5 * 5000 * 2
for c in range(0, max(X, Y) + 1):
    v = 0
    v += (c * 2) * C
    if c < X:
        v += (X - c) * A
    if c < Y:
        v += (Y - c) * B
    if v < min_v:
        min_v = v
print(int(min_v))