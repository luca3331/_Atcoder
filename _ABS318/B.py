N = int(input())
ABCD = set()
for n in range(N):
    a, b, c, d = map(int, input().split())
    for i in range(c, d):
        for j in range(a, b):
            if not (i, j) in ABCD:
                ABCD.add((i, j))
print(len(ABCD))