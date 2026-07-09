import numpy as np

# Create a 3x3 array with random integers from 1 to 20
array = np.random.randint(1, 21, size=(3, 3))

print("Original Array:")
print(array)

# Create a mask for diagonal elements
mask = np.eye(3, dtype=bool)

# Create masked array
masked_array = np.ma.array(array, mask=mask)

print("\nMasked Array:")
print(masked_array)

# Calculate mean of unmasked elements
mean_value = masked_array.mean()

# Replace masked elements with the mean
filled_array = masked_array.filled(mean_value)

print("\nMean of Unmasked Elements:")
print(mean_value)

print("\nFinal Array:")
print(filled_array)