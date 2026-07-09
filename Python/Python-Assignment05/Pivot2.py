import pandas as pd
import numpy as np

# Create DataFrame
df = pd.DataFrame({
    'Year': [2022, 2022, 2022, 2022,
             2023, 2023, 2023, 2023],
    'Quarter': ['Q1', 'Q2', 'Q3', 'Q4',
                'Q1', 'Q2', 'Q3', 'Q4'],
    'Revenue': np.random.randint(5000, 15000, size=8)
})

print("Original DataFrame:")
print(df)

# Create Pivot Table
pivot_table = pd.pivot_table(
    df,
    values='Revenue',
    index='Year',
    columns='Quarter',
    aggfunc='mean'
)

print("\nPivot Table:")
print(pivot_table)