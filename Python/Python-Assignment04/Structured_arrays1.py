import numpy as np

# Define the structured data type
student_dtype = [('name', 'U20'), ('age', 'i4'), ('weight', 'f4')]

# Create the structured array
students = np.array([
    ('Sneha', 22, 55.5),
    ('Rahul', 20, 68.2),
    ('Anjali', 24, 52.8),
    ('Rohan', 21, 70.0)
], dtype=student_dtype)

print("Original Structured Array:")
print(students)

# Sort by age
sorted_students = np.sort(students, order='age')

print("\nSorted by Age:")
print(sorted_students)