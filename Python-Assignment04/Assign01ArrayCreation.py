import numpy as np

# Create a 5x5 array with random integers from 1 to 20
arr = np.random.randint(1, 21, size=(5, 5))

print("Original Array:")
print(arr)

# Replace the third column (index 2) with 1
arr[:, 2] = 1

print("\nArray after replacing the third column with 1:")
print(arr)