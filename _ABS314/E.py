from collections import defaultdict, deque

N = int(input())
G = defaultdict(list)
in_degrees = [0 for _ in range(N + 1)]
appear_books = {1}
for n in range(1, N + 1):
    tmp = input().split()
    for t in tmp[1:]:
        G[n].append(int(t))
        appear_books.add(int(t))
        appear_books.add(int(n))

# print(G)

def topological_sort():
    # グラフに出現する本の中で，入次元が0のものを探す
    # zero_in_degrees = []
    queue = deque()
    for key in G.keys():
        for node in G[key]:
            in_degrees[node] += 1
    # for book in appear_books:
    #     if in_degrees[book] == 0:
    #         queue.append(book)
    queue.extend([1])

    sorted_order = []
    while queue:
        node = queue.popleft()
        sorted_order.append(node)
        for neighbor in G[node]:
            in_degrees[neighbor] -= 1
            if in_degrees[neighbor] == 0:
                queue.append(neighbor)
    return sorted_order

order = topological_sort()
order.reverse()
print(*order[:-1])
