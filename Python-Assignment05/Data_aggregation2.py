import pandas as pd
import numpy as np

# Create sample data
products = ['Laptop', 'Phone', 'Tablet', 'Monitor', 'Keyboard', 'Mouse']

categories = np.random.choice(
    ['Electronics', 'Accessories'],
    size=6
)

sales = np.random.randint(1000, 10000, size=6)

df = pd.DataFrame({
    'Product': products,
    'Category': categories,
    'Sales': sales
})

print("Original DataFrame:")
print(df)

# Group by Category and calculate total sales
total_sales = df.groupby('Category')['Sales'].sum()

print("\nTotal Sales by Category:")
print(total_sales)