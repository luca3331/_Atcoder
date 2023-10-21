N = int(input())
S = list(input().split())
if 'o' in S and not 'x' in S:
    print('Yes')
else:
    print('No')