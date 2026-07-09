import numpy as np

# Create two 3x4 arrays with random integers from 1 to 10
array1 = np.random.randint(1, 11, size=(3, 4))
array2 = np.random.randint(1, 11, size=(3, 4))

print("Array 1:")
print(array1)

print("\nArray 2:")
print(array2)

# Element-wise Addition
print("\nAddition:")
print(array1 + array2)

# Element-wise Subtraction
print("\nSubtraction:")
print(array1 - array2)

# Element-wise Multiplication
print("\nMultiplication:")
print(array1 * array2)

# Element-wise Division
print("\nDivision:")
print(array1 / array2)