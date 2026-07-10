# MNIST Handwritten Digit Classification using PyTorch

import torch
import torch.nn as nn
import torch.optim as optim

from torchvision import datasets, transforms
from torch.utils.data import DataLoader

# ---------------------------------------
# Step 1: Load and Normalize Dataset
# ---------------------------------------

transform = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize((0.1307,), (0.3081,))
])

train_dataset = datasets.MNIST(
    root="./data",
    train=True,
    download=True,
    transform=transform
)

test_dataset = datasets.MNIST(
    root="./data",
    train=False,
    download=True,
    transform=transform
)

train_loader = DataLoader(
    train_dataset,
    batch_size=64,
    shuffle=True
)

test_loader = DataLoader(
    test_dataset,
    batch_size=64,
    shuffle=False
)

# ---------------------------------------
# Step 2: Define Neural Network
# ---------------------------------------

class DigitClassifier(nn.Module):

    def __init__(self):
        super(DigitClassifier, self).__init__()

        self.fc1 = nn.Linear(28 * 28, 128)   # Input Layer
        self.relu = nn.ReLU()                # Hidden Layer
        self.fc2 = nn.Linear(128, 10)        # Output Layer

    def forward(self, x):

        # Flatten image (28x28 -> 784)
        x = x.view(-1, 28 * 28)

        x = self.fc1(x)
        x = self.relu(x)
        x = self.fc2(x)

        return x

# Create model
model = DigitClassifier()

# ---------------------------------------
# Step 3: Loss Function and Optimizer
# ---------------------------------------

criterion = nn.CrossEntropyLoss()

optimizer = optim.Adam(
    model.parameters(),
    lr=0.001
)

# ---------------------------------------
# Step 4: Train Model
# ---------------------------------------

epochs = 10

for epoch in range(epochs):

    running_loss = 0.0

    for images, labels in train_loader:

        outputs = model(images)

        loss = criterion(outputs, labels)

        optimizer.zero_grad()

        loss.backward()

        optimizer.step()

        running_loss += loss.item()

    avg_loss = running_loss / len(train_loader)

    print(f"Epoch [{epoch+1}/{epochs}] Loss: {avg_loss:.4f}")

# ---------------------------------------
# Step 5: Evaluate Model
# ---------------------------------------

correct = 0
total = 0

model.eval()

with torch.no_grad():

    for images, labels in test_loader:

        outputs = model(images)

        _, predicted = torch.max(outputs, 1)

        total += labels.size(0)

        correct += (predicted == labels).sum().item()

accuracy = (correct / total) * 100

print("\n==============================")
print(f"Test Accuracy: {accuracy:.2f}%")
print("==============================")