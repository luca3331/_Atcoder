from collections import defaultdict
N = int(input())
Q = int(input())
q = []
box = defaultdict(set())
for i in range(Q):
    query = input().split()
    if query[0] == '1':
        box[query[1]].add(query[2])
    if query[0] == '2':
        print(*sorted(box[query[1]]),sep='')
    if query[0] == '3':
        #