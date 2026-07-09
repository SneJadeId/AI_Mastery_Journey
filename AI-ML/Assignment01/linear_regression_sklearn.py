# linear_regression_sklearn.py

import pandas as pd
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Load dataset
housing = fetch_california_housing()

X = housing.data
y = housing.target

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Feature Scaling
scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Train Model
model = LinearRegression()

model.fit(X_train, y_train)

# Prediction
y_pred = model.predict(X_test)

# Results
print("=" * 50)
print("LINEAR REGRESSION USING SCIKIT-LEARN")
print("=" * 50)

print("\nIntercept:")
print(model.intercept_)

print("\nCoefficients:")
for feature, coef in zip(housing.feature_names, model.coef_):
    print(f"{feature:15s}: {coef:.6f}")

print("\nModel Performance")
print("-------------------------")
print("Mean Squared Error :", mean_squared_error(y_test, y_pred))
print("R2 Score           :", r2_score(y_test, y_pred))