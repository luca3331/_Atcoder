from collections import deque
S = deque(input())
stack = deque()
while len(S):
    stack.append(S.popleft())

    if len(stack) >= 3 and stack[-1] == 'C' and stack[-2] == 'B' and stack[-3] == 'A':
        stack.pop()
        stack.pop()
        stack.pop()
print(*stack, sep='')