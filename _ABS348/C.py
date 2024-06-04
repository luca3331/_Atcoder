from collections import defaultdict
N = int(input())

AC = [list(map(int, input().split())) for _ in range(N)]

D = defaultdict(int)
max_index = 0
max_a = AC[0][0]
for ac in AC[1]:
    a, c = ac[0], ac[1]
    if c in D.keys():
print(AC)