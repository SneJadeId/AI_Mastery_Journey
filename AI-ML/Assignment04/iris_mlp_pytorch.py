# iris_mlp_pytorch.py

import torch
import torch.nn as nn
import torch.optim as optim

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# ----------------------------------------
# Step 1: Load Iris Dataset
# ----------------------------------------

iris = load_iris()

X = iris.data
y = iris.target

# ----------------------------------------
# Step 2: Train-Test Split
# ----------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)

# ----------------------------------------
# Step 3: Feature Scaling
# ----------------------------------------

scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# ----------------------------------------
# Step 4: Convert Data to Tensors
# ----------------------------------------

X_train = torch.FloatTensor(X_train)
X_test = torch.FloatTensor(X_test)

y_train = torch.LongTensor(y_train)
y_test = torch.LongTensor(y_test)

# ----------------------------------------
# Step 5: Define Neural Network
# ----------------------------------------

class IrisNet(nn.Module):

    def __init__(self):
        super(IrisNet, self).__init__()

        self.fc1 = nn.Linear(4, 16)      # Input Layer
        self.relu = nn.ReLU()            # Hidden Layer Activation
        self.fc2 = nn.Linear(16, 3)      # Output Layer

    def forward(self, x):

        x = self.fc1(x)
        x = self.relu(x)
        x = self.fc2(x)

        return x

# Create Model
model = IrisNet()

# ----------------------------------------
# Step 6: Loss Function and Optimizer
# ----------------------------------------

criterion = nn.CrossEntropyLoss()

optimizer = optim.Adam(
    model.parameters(),
    lr=0.01
)

# ----------------------------------------
# Step 7: Train the Model
# ----------------------------------------

epochs = 100

for epoch in range(epochs):

    outputs = model(X_train)

    loss = criterion(outputs, y_train)

    optimizer.zero_grad()

    loss.backward()

    optimizer.step()

    if (epoch + 1) % 10 == 0:
        print(f"Epoch [{epoch+1}/{epochs}] Loss: {loss.item():.4f}")

# ----------------------------------------
# Step 8: Evaluate the Model
# ----------------------------------------

with torch.no_grad():

    outputs = model(X_test)

    _, predicted = torch.max(outputs, 1)

    correct = (predicted == y_test).sum().item()

    total = y_test.size(0)

    accuracy = (correct / total) * 100

print("\n===============================")
print("Test Accuracy: {:.2f}%".format(accuracy))
print("===============================")