from itertools import product
import re
N, K = map(int, input().split())
S = ''.join(input())
question = S.count('?')
kaibun = []
def make_kaibun(K):
    tmp = set()
    for elem in product(['A', 'B'], repeat= K // 2):
        elem += elem[::-1] 
        tmp.add(''.join(elem))
    return list(tmp)
kaibun = make_kaibun(K)
ct = 0
for i in range(N - K):
    substring = S[i:i+K]
    pattern = re.sub(r'\?', '.', substring)
    for kb in kaibun:
        if re.search(pattern, kb):
            print(kb, substring)
            ct += 1
            ct = ct % 998244353
print(kaibun)
print(ct)
print((2**question - ct) % 998244353)