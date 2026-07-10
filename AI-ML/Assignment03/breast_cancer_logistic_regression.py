# Breast Cancer Classification using Logistic Regression

import matplotlib.pyplot as plt

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    confusion_matrix,
    ConfusionMatrixDisplay,
    classification_report,
    roc_curve,
    roc_auc_score
)

# ----------------------------------------------------
# Step 1: Load Dataset
# ----------------------------------------------------

data = load_breast_cancer()

X = data.data
y = data.target

print("Dataset Shape:", X.shape)
print("Classes:", data.target_names)

# ----------------------------------------------------
# Step 2: Train-Test Split
# ----------------------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)

# ----------------------------------------------------
# Step 3: Feature Scaling
# ----------------------------------------------------

scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# ----------------------------------------------------
# Step 4: Train Logistic Regression Model
# ----------------------------------------------------

model = LogisticRegression(random_state=42)

model.fit(X_train, y_train)

# ----------------------------------------------------
# Step 5: Prediction
# ----------------------------------------------------

y_pred = model.predict(X_test)
y_prob = model.predict_proba(X_test)[:, 1]

# ----------------------------------------------------
# Step 6: Confusion Matrix
# ----------------------------------------------------

cm = confusion_matrix(y_test, y_pred)

print("\nConfusion Matrix")
print(cm)

disp = ConfusionMatrixDisplay(
    confusion_matrix=cm,
    display_labels=data.target_names
)

disp.plot(cmap="Blues")
plt.title("Confusion Matrix")
plt.show()

# ----------------------------------------------------
# Step 7: Classification Report
# ----------------------------------------------------

print("\nClassification Report")
print(classification_report(
    y_test,
    y_pred,
    target_names=data.target_names
))

# ----------------------------------------------------
# Step 8: ROC Curve and AUC Score
# ----------------------------------------------------

fpr, tpr, thresholds = roc_curve(y_test, y_prob)

auc_score = roc_auc_score(y_test, y_prob)

print("AUC Score:", auc_score)

plt.figure(figsize=(6,5))

plt.plot(fpr, tpr, label=f"AUC = {auc_score:.4f}")

plt.plot([0,1], [0,1], linestyle="--")

plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("ROC Curve")

plt.legend()

plt.show()