# linear_regression_from_scratch.py

import numpy as np
import pandas as pd

from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Load Dataset
housing = fetch_california_housing()

X = housing.data
y = housing.target

# Split Dataset
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

# ==========================
# Linear Regression From Scratch
# ==========================

class LinearRegressionGD:

    def __init__(self, learning_rate=0.01, iterations=5000):
        self.learning_rate = learning_rate
        self.iterations = iterations

    def fit(self, X, y):

        m, n = X.shape

        self.weights = np.zeros(n)
        self.bias = 0

        for i in range(self.iterations):

            y_pred = np.dot(X, self.weights) + self.bias

            dw = (1 / m) * np.dot(X.T, (y_pred - y))
            db = (1 / m) * np.sum(y_pred - y)

            self.weights = self.weights - self.learning_rate * dw
            self.bias = self.bias - self.learning_rate * db

    def predict(self, X):
        return np.dot(X, self.weights) + self.bias


# Train Custom Model
custom_model = LinearRegressionGD()

custom_model.fit(X_train, y_train)

custom_predictions = custom_model.predict(X_test)

# Train Sklearn Model for Comparison
sklearn_model = LinearRegression()

sklearn_model.fit(X_train, y_train)

# ==========================
# Results
# ==========================

print("=" * 60)
print("CUSTOM LINEAR REGRESSION (GRADIENT DESCENT)")
print("=" * 60)

print("\nIntercept:")
print(custom_model.bias)

print("\nCoefficients:")
for feature, coef in zip(housing.feature_names, custom_model.weights):
    print(f"{feature:15s}: {coef:.6f}")

print("\nPerformance")
print("-------------------------")
print("Mean Squared Error :", mean_squared_error(y_test, custom_predictions))
print("R2 Score           :", r2_score(y_test, custom_predictions))

# ==========================
# Comparison
# ==========================

print("\n")
print("=" * 60)
print("COMPARISON WITH SCIKIT-LEARN")
print("=" * 60)

comparison = pd.DataFrame({
    "Feature": housing.feature_names,
    "Scikit-Learn": sklearn_model.coef_,
    "Custom Model": custom_model.weights
})

print(comparison)

print("\nIntercept Comparison")
print("---------------------------")
print("Scikit-learn :", sklearn_model.intercept_)
print("Custom Model :", custom_model.bias)