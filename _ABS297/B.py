import numpy
import numpy as np
N = int(input())
A = []
B = []
flag = False
for n in range(N):
    A.append(list(map(int, input().split())))
for n in range(N):
    B.append(list(map(int, input().split())))
A = np.array(A)
B = np.array(B)

for i in range(4):
    if A.all() == B.all():
        flag = True
        break
    else:
        A = np.rot90(A)
if flag:
    print('Yes')
else:
    print('No')