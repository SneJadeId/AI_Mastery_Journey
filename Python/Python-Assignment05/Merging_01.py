import pandas as pd

# Create first DataFrame
df1 = pd.DataFrame({
    'ID': [101, 102, 103, 104],
    'Name': ['Sneha', 'Rahul', 'Anjali', 'Rohan']
})

# Create second DataFrame
df2 = pd.DataFrame({
    'ID': [101, 102, 103, 104],
    'Marks': [85, 90, 78, 88]
})

print("DataFrame 1:")
print(df1)

print("\nDataFrame 2:")
print(df2)

# Merge using the common column 'ID'
merged_df = pd.merge(df1, df2, on='ID')

print("\nMerged DataFrame:")
print(merged_df)