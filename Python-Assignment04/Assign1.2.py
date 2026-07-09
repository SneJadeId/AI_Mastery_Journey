import numpy as np

# Create a 4x4 array with values from 1 to 16
arr = np.arange(1, 17).reshape(4, 4)

print("Original Array:")
print(arr)

# Replace diagonal elements with 0
np.fill_diagonal(arr, 0)

print("\nModified Array:")
print(arr)