import re

N = int(input())
S = input()
if re.search('MM|FF', S):
    print('No')
else:
    print('Yes')