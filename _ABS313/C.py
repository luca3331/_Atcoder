from collections import defaultdict
N, M = map(int, input().split())
S = input()
C = input().split()
D = defaultdict(list)

for i, s in enumerate (S):
    D[C[i]].append([i, s])

print(D)

order = [0] * len(N)
for key in D.keys():
    l = D[key]
    tmp = l[len(l)][0]
    for i, v in enumerate(l[1:]):
        l[i][0] = l[i]
