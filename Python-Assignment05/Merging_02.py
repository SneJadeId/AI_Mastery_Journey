import pandas as pd

# Create first DataFrame
df1 = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6]
})

# Create second DataFrame
df2 = pd.DataFrame({
    'C': [7, 8, 9],
    'D': [10, 11, 12]
})

print("DataFrame 1:")
print(df1)

print("\nDataFrame 2:")
print(df2)

# Concatenate along rows
row_concat = pd.concat([df1, df2], axis=0)

print("\nConcatenated Along Rows:")
print(row_concat)

# Concatenate along columns
column_concat = pd.concat([df1, df2], axis=1)

print("\nConcatenated Along Columns:")
print(column_concat)