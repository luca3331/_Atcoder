N = int(input())
div = []
m = 100
for i in range(1, int(N / 2) + 1):
    if N % i == 0:
        div.append([i, N // i])
    if i >= N // i:
        break
for x in div:
    digit = max(len(str(x[0])), len(str(x[1])))
    if m > digit:
        m = digit
print(m)
