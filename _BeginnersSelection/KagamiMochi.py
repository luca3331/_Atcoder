num = int(input())
elements = []
for _ in range(num):
    elements.append(int(input()))
print(len(set(elements)))