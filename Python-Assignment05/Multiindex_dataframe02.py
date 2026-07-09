import pandas as pd
import numpy as np

# MultiIndex
index = pd.MultiIndex.from_tuples([
    ('Electronics', 'Mobile'),
    ('Electronics', 'Laptop'),
    ('Furniture', 'Chair'),
    ('Furniture', 'Table'),
    ('Clothing', 'Men'),
    ('Clothing', 'Women')
], names=['Category', 'SubCategory'])

# Create DataFrame
df = pd.DataFrame({
    'Sales': np.random.randint(1000, 10000, size=6)
}, index=index)

print("DataFrame:")
print(df)

# Sum by Category
print("\nSum by Category:")
print(df.groupby(level='Category').sum())

# Sum by Category and SubCategory
print("\nSum by Category and SubCategory:")
print(df.groupby(level=['Category', 'SubCategory']).sum())