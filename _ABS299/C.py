import re
N = int(input())
S = input()
reg = re.compile(r'o+\-|\-o+')
candidate = re.findall(reg, S)

if candidate:
    print(max(len(c) for c in candidate) - 1)
else:
    print('-1')

