from collections import deque, defaultdict
import itertools
l = [1, 2, 3]
M = int(input())
S1 = deque(input())
S2 = deque(input())
S3 = deque(input())

S1_d = defaultdict(list)
S2_d = defaultdict(list)
S3_d = defaultdict(list)

for i, s in enumerate(S1):
    S1_d[s].append(i)
for i, s in enumerate(S2):
    S2_d[s].append(i)
for i, s in enumerate(S3):
    S3_d[s].append(i)

for n in range(10):
    if n in S1 and n in S2 and n in S3:
        p = itertools.permutations(l)
        for v in p:
            t = 0
            if v == 1:
                if n in S1_d.keys():
    else:
        continue
for t in range(M):
    tt = t
    n = str(S1[t])
    if n in S1 and n in S2 and n in S3:
        tt += max(S2_d[n][0], 
