from collections import defaultdict

N = int(input())
F = defaultdict(list)
max_values = []
ans = -1
for _ in range(N):
    f, s = map(int, input().split())
    F[f].append(s)

for f in F:
    max_values.append(max(F[f]))

max_values.sort(reverse=True)

for c in F.values():
    c.sort(reverse=True)
    if len(c) >= 2:
        ans = max(ans, c[0] + c[1] // 2)
if len(max_values) >= 2:
    ans = max(ans, max_values[0] + max_values[1])
print(int(ans))