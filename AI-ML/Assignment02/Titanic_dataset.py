# Titanic Data Preprocessing and Model Comparison

import pandas as pd
import seaborn as sns

from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.metrics import accuracy_score

from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier

# ------------------------------------------
# Step 1: Load Dataset
# ------------------------------------------

# Load Titanic dataset
df = sns.load_dataset("titanic")

# Keep only required columns
df = df[['survived', 'pclass', 'sex', 'age', 'fare', 'embarked']]

print("First 5 Rows")
print(df.head())

print("\nMissing Values")
print(df.isnull().sum())

# ------------------------------------------
# Step 2: Handle Missing Values
# ------------------------------------------

df['age'] = df['age'].fillna(df['age'].mean())

df['embarked'] = df['embarked'].fillna(df['embarked'].mode()[0])

print("\nMissing Values After Imputation")
print(df.isnull().sum())

# ------------------------------------------
# Step 3: Categorical Encoding
# ------------------------------------------

# Label Encoding for sex
le = LabelEncoder()
df['sex'] = le.fit_transform(df['sex'])

# One-Hot Encoding for embarked
df = pd.get_dummies(df, columns=['embarked'], dtype=int)

print("\nEncoded Dataset")
print(df.head())

# ------------------------------------------
# Step 4: Feature Scaling
# ------------------------------------------

scaler = StandardScaler()

df[['age', 'fare']] = scaler.fit_transform(df[['age', 'fare']])

print("\nScaled Dataset")
print(df.head())

# ------------------------------------------
# Step 5: Train-Test Split
# ------------------------------------------

X = df.drop('survived', axis=1)
y = df['survived']

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)

print("\nTraining Samples :", len(X_train))
print("Testing Samples  :", len(X_test))

# ------------------------------------------
# Model Training
# ------------------------------------------

models = {
    "Logistic Regression": LogisticRegression(max_iter=1000),
    "Decision Tree": DecisionTreeClassifier(random_state=42),
    "Random Forest": RandomForestClassifier(random_state=42)
}

print("\nModel Comparison")
print("-" * 45)

for name, model in models.items():

    # Cross Validation
    cv_score = cross_val_score(
        model,
        X_train,
        y_train,
        cv=5,
        scoring='accuracy'
    )

    # Train Model
    model.fit(X_train, y_train)

    # Prediction
    y_pred = model.predict(X_test)

    # Accuracy
    test_acc = accuracy_score(y_test, y_pred)

    print(f"{name}")
    print(f"Cross Validation Accuracy : {cv_score.mean():.4f}")
    print(f"Test Accuracy             : {test_acc:.4f}")
    print("-" * 45)