import numpy as np

# Create a 2x3 matrix
matrix1 = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

# Create a 3x2 matrix
matrix2 = np.array([
    [7, 8],
    [9, 10],
    [11, 12]
])

print("Matrix 1:")
print(matrix1)

print("\nMatrix 2:")
print(matrix2)

# Matrix multiplication
result = np.matmul(matrix1, matrix2)

print("\nMatrix Multiplication Result:")
print(result)