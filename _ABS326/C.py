import bisect
N, M = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
res = 0
for i, a in enumerate(A):
    v = bisect.bisect_left(A, A[i] + M)
    res = max(res, v - i)
print(res)