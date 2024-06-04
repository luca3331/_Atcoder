from collections import defaultdict
N = int(input())
A = list(map(int, input().split()))
D = defaultdict(int)
for a in A:
    D[a] += 1
T = [0] * (max(D.keys()) + 1)
keys = sorted(D.keys(), reverse=True)
for i in range(1, len(keys)):
    T[keys[i]] = keys[i-1] * D[keys[i-1]] + T[keys[i-1]]

for a in A:
    print(T[a])