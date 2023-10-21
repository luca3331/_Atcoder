N = int(input())
a = 0
ans = 0

# for i in range(105, N + 2, 2):
#     for j in range(1, int(i / 2)):
#         if i % j == 0:
#             a += 1
#             # print(j)
#     if a == 7: #整数Nは自身を約数として持つが，jのfor文はiの真ん中までしか走らないので帳尻合わせで8-1
#         ans += 1
#     a = 0
for i in range(1, N + 1):
    for j in range(1, i + 1):
        if i % j == 0:
            a += 1
    if a == 8 and i % 2 == 1:
        ans += 1
    a = 0
print(ans)
