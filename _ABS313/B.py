from collections import defaultdict
N = int(input())
C = []
A = []
deme = defaultdict(list)

for n in range(N):
    C.append(int(input()))
    AA = list(input().split())
    A.append(AA)
    for a in AA:
        deme[a].append(n)

X = int(input())

# print(C)

order = []
new_order = []
if len(deme[str(X)]) == 0:
    print(0)
else:
    for member in deme[str(X)]:
        # print(member)
        order.append([member, C[member]])
    min_value = min(order, key=lambda x: x[1])[1]
    for ord in order:
        if ord[1] == min_value:
            new_order.append(ord[0] + 1)

    print(len(new_order))
    print(*new_order)