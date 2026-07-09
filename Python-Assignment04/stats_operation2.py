import numpy as np

# Create a 3x3 array with values from 1 to 9
array = np.arange(1, 10).reshape(3, 3)

print("Original Array:")
print(array)

# Calculate mean and standard deviation
mean = np.mean(array)
std_dev = np.std(array)

# Normalize the array
normalized_array = (array - mean) / std_dev

print("\nNormalized Array:")
print(normalized_array)

print("\nMean of Normalized Array:", np.mean(normalized_array))
print("Standard Deviation of Normalized Array:", np.std(normalized_array))