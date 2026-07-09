import numpy as np

# Create a 5x5 array with random integers from 1 to 20
array = np.random.randint(1, 21, size=(5, 5))

print("Original Array:")
print(array)

# Calculate statistical measures
mean = np.mean(array)
median = np.median(array)
std_dev = np.std(array)
variance = np.var(array)

print("\nMean:", mean)
print("Median:", median)
print("Standard Deviation:", std_dev)
print("Variance:", variance)