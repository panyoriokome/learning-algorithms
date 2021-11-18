def flawed(A):
    my_max = A[0]
    for idx in range(1, len(A)):
        if my_max < A[idx]:
            my_max = A[idx]
        return my_max

print(flawed([0, 1]))
print(flawed([1, 0]))