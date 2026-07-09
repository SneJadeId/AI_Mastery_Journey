import numpy as np

# Create a 4x4 array with random integers from 1 to 20
array_2d = np.random.randint(1, 21, size=(4, 4))

# Create a 1D array
array_1d = np.array([1, 2, 3, 4])

print("Original Array:")
print(array_2d)

print("\n1D Array:")
print(array_1d)

# Broadcasting subtraction
result = array_2d - array_1d[:, np.newaxis]

print("\nResult after Broadcasting Subtraction:")
print(result)