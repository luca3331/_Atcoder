import heapq
from collections import defaultdict
N, M, L = map(int, input().split())
A = list(enumerate(list(map(int, input().split()))))
B = sorted(list(enumerate(list(map(int, input().split())))), reverse=True, key= lambda x:x[1])
D = defaultdict(list)
S = set()
for nl in range(L):
    c, d = map(int, input().split())
    S.add((c, d))
# print(D)
# menus = [[a[1] + b[1] for a in A if b[0] + 1 not in (D[a[0]] + 1)] for b in B]
menus = []
ans = 0
for a in A:
    for b in B:
        if (a[0] + 1, b[0] + 1) not in S:
            if a[1] + b[1] > ans:
                ans = a[1] + b[1]
            break
print(ans)
