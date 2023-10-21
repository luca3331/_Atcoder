from itertools import permutations
import math
ele = [x for x in range(1, 10)]
order = list(permutations(ele, 9))
all_order = len(order)
C = [input().split() for x in range(3)]
danger = []
for i in range(3):
    if C[i][0] == C[i][1] or C[i][1] == C[i][2] or C[i][0] == C[i][2]:
        danger.append(i)
for j in range(3):
    if C[0][j] == C[1][j] or C[0][j] == C[2][j] or C[1][j] == C[2][j]:
        danger.append(i + 3)
if C[0][0] ==
print(C)

