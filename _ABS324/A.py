N = int(input())
A = input().split()
flag = True

for i in range(len(A) - 1):
    if A[i] == A[i + 1]:
        continue
    else:
        flag = False

if flag:
    print('Yes')
else:
    print('No')