import numpy as np

# Create a 4x4 array with random integers from 1 to 20
array = np.random.randint(1, 21, size=(4, 4))

print("Original Array:")
print(array)

# Create a masked array
masked_array = np.ma.masked_greater(array, 10)

print("\nMasked Array:")
print(masked_array)

# Compute the sum of unmasked elements
print("\nSum of Unmasked Elements:")
print(masked_array.sum())