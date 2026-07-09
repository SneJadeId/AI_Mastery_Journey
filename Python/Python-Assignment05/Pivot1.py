import pandas as pd
import numpy as np

# Create DataFrame
df = pd.DataFrame({
    'Date': ['2024-01-01', '2024-01-01', '2024-01-02',
             '2024-01-02', '2024-01-03', '2024-01-03'],
    'Category': ['A', 'B', 'A', 'B', 'A', 'B'],
    'Value': np.random.randint(10, 100, size=6)
})

print("Original DataFrame:")
print(df)

# Create Pivot Table
pivot_table = pd.pivot_table(
    df,
    values='Value',
    index='Date',
    columns='Category',
    aggfunc='sum'
)

print("\nPivot Table:")
print(pivot_table)