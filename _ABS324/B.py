N = int(input())
while True:
    if N % 2 == 0:
        N = N // 2
    else:
        break

while True:
    if N % 3 == 0:
        N = N // 3
    else:
        break

if N == 1:
    print('Yes')
else:
    print('No')