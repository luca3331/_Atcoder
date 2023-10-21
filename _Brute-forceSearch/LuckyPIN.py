N = int(input())
S = str(input())
psw = set()
# for i in range(N):#悪い例 30000 ** 3で草
#     for j in range(i + 1, N):
#         for k in range(j + 1, N):
#             psw.add(S[i] + S[j] + S[k])

for n in range(1000):
    i, j, k = list(str(n).zfill(3))
    i_id = S.find(i)
    if i_id == -1:
        continue
    j_id = S.find(j, i_id + 1)
    if j_id == -1:
        continue
    k_id = S.find(k, j_id + 1)
    if k_id == -1:
        continue
    psw.add(S[i_id] + S[j_id] + S[k_id])

print(len(psw))