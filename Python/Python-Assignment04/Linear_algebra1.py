import numpy as np

# Create a 3x3 matrix
matrix = np.array([
    [2, 1, 3],
    [1, 4, 2],
    [3, 2, 5]
])

print("Matrix:")
print(matrix)

# Determinant
det = np.linalg.det(matrix)

# Inverse
inverse = np.linalg.inv(matrix)

# Eigenvalues
eigenvalues = np.linalg.eigvals(matrix)

print("\nDeterminant:")
print(det)

print("\nInverse:")
print(inverse)

print("\nEigenvalues:")
print(eigenvalues)