N, X = input().split()
S = list(map(int, input().split()))
sum_score  = 0
for s in S:
    if int(X) >= s:
        sum_score += s
print(sum_score)