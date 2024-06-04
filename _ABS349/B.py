from collections import Counter
S = input()
c = Counter(S)
T = [0] * 101
for ele in c:
    T[c[ele]] += 1
# print(T)
print('Yes' if all(t in (0, 2) for t in T) else 'No')
# for t in T:
#     if t != 2 and t != 0:
#         print('No')
#         exit()
# print('Yes')