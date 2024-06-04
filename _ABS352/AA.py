A = [2**i for i in range(35)]
B = [A[i - 1] + A[i] for i in range(len(A))]
print(B)
