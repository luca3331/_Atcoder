import collections

N = int(input())
A = map(int, input().split())
c = collections.Counter(A)
ans = 0
for i in c.values():
    ans += i // 2
print(ans)