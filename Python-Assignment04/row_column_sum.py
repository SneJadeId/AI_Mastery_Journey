import numpy as np

# Create a 4x4 array with values from 1 to 16
array = np.arange(1, 17).reshape(4, 4)

print("Original Array:")
print(array)

# Row-wise Sum
row_sum = np.sum(array, axis=1)

# Column-wise Sum
column_sum = np.sum(array, axis=0)

print("\nRow-wise Sum:")
print(row_sum)

print("\nColumn-wise Sum:")
print(column_sum)