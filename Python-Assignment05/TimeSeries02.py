import pandas as pd
import numpy as np

# Create date range
dates = pd.date_range(start='2021-01-01', end='2021-12-31')

# Create DataFrame
df = pd.DataFrame({
    'Value': np.random.randint(1, 101, size=len(dates))
}, index=dates)

print("Original DataFrame:")
print(df.head(10))

# Compute rolling mean
df['Rolling Mean'] = df['Value'].rolling(window=7).mean()

print("\nDataFrame with 7-Day Rolling Mean:")
print(df.head(15))