N = input()
S = input()
flag = False
for i in range(len(S) - 1):
    if S[i] == 'a' and S[i + 1] == 'b' or S[i] == 'b' and S[i + 1] == 'a':
        flag = True

if flag:
    print('Yes')
else:
    print('No')
