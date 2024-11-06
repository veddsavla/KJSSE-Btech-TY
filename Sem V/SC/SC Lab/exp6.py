import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

print("Script is running...")

# XOR inputs (features) and targets (labels)
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([[0], [1], [1], [0]])

# Build the MLP model
model = Sequential()

# Input layer with 2 neurons, hidden layer with 2 neurons (ReLU activation)
model.add(Dense(2, input_dim=2, activation="relu"))

# Output layer with 1 neuron (Sigmoid activation for binary output)
model.add(Dense(1, activation="sigmoid"))

# Compile the model with binary crossentropy loss and Adam optimizer
model.compile(loss="binary_crossentropy", optimizer="adam", metrics=["accuracy"])

# Train the model (verbose=0 to suppress output)
model.fit(X, y, epochs=1000, verbose=0)

# Evaluate the model accuracy on the XOR inputs
_, accuracy = model.evaluate(X, y)
print(f"Model Accuracy: {accuracy * 100:.2f}%")

# Predict the outputs for the XOR inputs
predictions = model.predict(X)
predictions = np.round(predictions)  # Round predictions for binary classification

# Print the predicted outputs
print(f"Predicted Outputs:\n{predictions}")
