N = list(input())
flag = True
for i in range(len(N) - 1):
    if not N[i] > N[i + 1]:
        flag = False

if flag:
    print('Yes')
else:
    print('No')