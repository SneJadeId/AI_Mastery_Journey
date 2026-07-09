import numpy as np

# Create a 3x3 array with random integers from 1 to 10
array_2d = np.random.randint(1, 11, size=(3, 3))

# Create a 1D array
array_1d = np.array([10, 20, 30])

print("2D Array:")
print(array_2d)

print("\n1D Array:")
print(array_1d)

# Broadcasting addition
result = array_2d + array_1d

print("\nResult after Broadcasting Addition:")
print(result)