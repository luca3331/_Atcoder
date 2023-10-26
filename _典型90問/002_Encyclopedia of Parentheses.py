from itertools import product
N = int(input())

def is_valid(S):
    score = 0
    for s in S:
        if s == '(':
            score += 1
        else:
            score -= 1
        if score < 0:
            return False
    if score == 0:
        return True

for S in product(['(', ')'], repeat=N):
    if is_valid(S):
        print(*S, sep='')
