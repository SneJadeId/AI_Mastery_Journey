import pandas as pd
import numpy as np

# Create DataFrame
categories = np.random.choice(['A', 'B', 'C'], size=10)
values = np.random.randint(10, 101, size=10)

df = pd.DataFrame({
    'Category': categories,
    'Value': values
})

print("Original DataFrame:")
print(df)

# Group by Category
result = df.groupby('Category')['Value'].agg(['sum', 'mean'])

print("\nSum and Mean of Value for each Category:")
print(result)