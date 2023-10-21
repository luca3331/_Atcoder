H, W = map(int, input().split())
A = []
for i in range(H):
    A.append(list(map(int, input().split())))

for i in range(H):
    txt = ""
    for j in range(W):
        if A[i][j] == 0:
            txt += '.'
        else:
            txt += chr(64 + A[i][j])
    print(txt)
