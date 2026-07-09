import numpy as np

# Define the structured data type
point_dtype = [('x', 'i4'), ('y', 'i4')]

# Create the structured array
points = np.array([
    (1, 2),
    (4, 6),
    (7, 3),
    (2, 8)
], dtype=point_dtype)

print("Points:")
print(points)

print("\nEuclidean Distances:")

# Compute distance between every pair of points
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        distance = np.sqrt(
            (points[i]['x'] - points[j]['x'])**2 +
            (points[i]['y'] - points[j]['y'])**2
        )

        print(f"Distance between Point {i+1} and Point {j+1}: {distance:.2f}")