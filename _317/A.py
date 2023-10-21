N, H, X = map(int, input().split())
P = list(map(int, input().split()))

for i, p in enumerate (P):
    if p >= X - H:
        print(i + 1)
        break