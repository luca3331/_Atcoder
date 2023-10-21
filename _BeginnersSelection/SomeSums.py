a, b, c = map(int, input().split())
count = 0
for ele in range(a + 1):
    digits = list(map(int, list(str(ele))))
    # print(digits, sum(digits))
    if b <= sum(digits) and sum(digits) <= c:
        count += ele
print(count)