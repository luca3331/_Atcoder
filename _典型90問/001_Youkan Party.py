N, L = map(int, input().split())
K = int(input())
A = list(map(int, input().split()))

import heapq

class PriorityQueue:
    def __init__(self):
        self.heap = []
        self.counter = 0

    def push(self, item, priority):
        entry = (priority, self.counter, item)
        heapq.heappush(self.heap, entry)
        self.counter += 1

    def pop(self):
        (_, _, item) = heapq.heappop(self.heap)
        return item

# 使用例
priority_queue = PriorityQueue()
priority_queue.push({'name': 'Alice'}, 2)
priority_queue.push({'name': 'Bob'}, 1)
priority_queue.push({'name': 'Charlie'}, 3)

print(priority_queue.pop())  # {'name': 'Bob'}
print(priority_queue.pop())  # {'name': 'Alice'}
print(priority_queue.pop())  # {'name': 'Charlie'}
