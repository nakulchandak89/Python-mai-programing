import tensorflow as tf
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense
import numpy as np

# Step 1: Prepare data
X_train = np.array([[0], [1], [2], [3], [4]], dtype=np.float32)
y_train = np.array([[0], [2], [4], [6], [8]], dtype=np.float32)

# Step 2: Define the model
model = Sequential([
    Dense(units=10, activation='relu', input_shape=(1,)),  # Hidden layer
    Dense(units=1)  # Output layer
])

# Step 3: Compile the model
model.compile(optimizer='adam', loss='mse', metrics=['mae'])

# Step 4: Train the model
model.fit(X_train, y_train, epochs=50, batch_size=1, verbose=1)

# Step 5: Evaluate the model
X_test = np.array([[5], [6]], dtype=np.float32)
y_test = np.array([[10], [12]], dtype=np.float32)
loss, mae = model.evaluate(X_test, y_test)
print(f"Loss: {loss}, MAE: {mae}")

# Step 6: Make predictions
predictions = model.predict(np.array([[7], [8]]))
print("Predictions:", predictions)
