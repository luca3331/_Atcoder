from collections import deque
N = int(input())
S = input().split()
Q = int(input())
query = deque()

state = [False] * N
for q in range(Q):
    query.append(input().split())

print(query)

while query:
    order = query.pop()

#大文字か小文字か[0, 1]
#文字[a-z]
#一番下の指示を見ればいい