S = list(input())
S1 = S.copy()
q1 = []
q2 = []
flag = True
for i, s in enumerate (S):
    if s == 'B':
        q1.append(i % 2)
    if s == 'R':
        q2.append(i)
    if s == 'K':
        q3 = i

if len(q1) < 2:
    flag = False
elif q1[0] == q1[1]:
    flag = False
elif not (q2[0] < q3 < q2[1]):
    flag = False
else:
    pass
if flag:
    print('Yes')
else:
    print('No')

