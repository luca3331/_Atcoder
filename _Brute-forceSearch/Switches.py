N, M = map(int, input().split())
data = []
for i in range(M):
    data = map(input().split())
p = list(map(int, input()))
ct = 0
flag = True
for n in range(2 ** N):
    sw = list(bin(n)[2:])
    for m in range(M):
        if not 'Mに繋がっているスイッチのうち，onになっているスイッチを2で割った個数がpiに等しい':
            flag = False
            break
    if not flag:
        continue