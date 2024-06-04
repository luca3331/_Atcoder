N = int(input())
A = list(map(int, input().split()))
pos = [0] * (N + 1)
sort_cd = []
for i, a in enumerate(A):
    pos[a] = i + 1

for i, p in enumerate(pos[:-1]):
    if i + 1 == pos[i + 1]:
        continue
    sort_cd.append((i + 1, pos[i + 1]))
    pos[pos[i + 1]] = pos[i + 1]
    pos[i + 1] = i + 1

print(len(sort_cd))
[print(f"{x} {y}") for x, y in sort_cd]
