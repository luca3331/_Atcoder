N = int(input())
A, B = zip(*(map(int, input().split()) for i in range(N)))
A = list(A)
B = list(B)
total_A = sum(A)
print(max([total_A - A[i] + B[i] for i in range(N)]))
