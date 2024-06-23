from collections import defaultdict
N = int(input())
A = list(map(int, input().split()))
D = defaultdict(list)
ct = 0
for i, a in enumerate(A):
    D[a].append(i+1)

for key in D.keys():
    if D[key][1] - D[key][0] == 2:
        ct += 1

print(ct)