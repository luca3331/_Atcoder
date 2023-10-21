N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
A_order = []
B_order = []
i = 1
C = []
while True:
    if len(A) == 0:
        while len(B) > 0:
            B_order.append(i)
            C.append([B.pop(0), i])
            i += 1
        break
    if len(B) == 0:
        while len(A) > 0:
            A_order.append(i)
            C.append([A.pop(0), i])
            i += 1
        break
    if A[0] < B[0]:
        A_order.append(i)
        C.append([A.pop(0), i])
    else:
        B_order.append(i)
        C.append([B.pop(0), i])
    i += 1
for a in A_order:
    print("{}".format(a), end=" ")
print("")
for b in B_order:
    print("{}".format(b), end=" ")
