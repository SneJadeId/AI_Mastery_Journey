import pandas as pd
import numpy as np

# Create date range
dates = pd.date_range(start='2021-01-01', periods=365, freq='D')

# Create DataFrame
df = pd.DataFrame({
    'Value': np.random.randint(1, 101, size=365)
}, index=dates)

print("Original DataFrame:")
print(df.head())

# Compute monthly mean
monthly_mean = df.resample('ME').mean()

print("\nMonthly Mean:")
print(monthly_mean)