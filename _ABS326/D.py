N = int(input())
R = input()
C = input()

from itertools import permutations, product

p = product(permutations(['A', 'B', 'C', '.', '.']), repeat=N)
# print(p)
ct = 0
for pp in p:
    ct += 1
    print(pp, ct)
    for i, ppp in enumerate(pp):
        for j in range(N):
            if ppp[j] != '.':
                if not ppp[j] == R[i]:
                    break
        else:
            continue
