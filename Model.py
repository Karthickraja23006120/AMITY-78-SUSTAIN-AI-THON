## PYTHON MODEL OF CARBON CALCULATOR
'''
import pandas as pd
import numpy as np
import tensorflow as tf
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv("synthetic_carbon_emission_data.csv")

# Features and target
X = data.drop("Carbon_Emission_tons_CO2e_per_year", axis=1)
y = data["Carbon_Emission_tons_CO2e_per_year"]

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Standardize the features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Define the neural network model
model = tf.keras.Sequential([
    tf.keras.layers.Dense(64, activation="relu", input_shape=(X_train.shape[1],)),
    tf.keras.layers.Dense(32, activation="relu"),
    tf.keras.layers.Dense(1)  # Output layer for regression
])

# Compile the model
model.compile(optimizer="adam", loss="mse", metrics=["mae"])

# Train the model
history = model.fit(X_train, y_train, epochs=50, batch_size=32, validation_split=0.2, verbose=1)

# Evaluate the model
test_loss, test_mae = model.evaluate(X_test, y_test, verbose=0)
print(f"Test Mean Absolute Error: {test_mae:.4f} tons CO2e/year")

# Make predictions
predictions = model.predict(X_test)

# Display predictions with total carbon consumed
print("Sample Predictions:")
total_consumed = 0
for i in range(5):
    predicted = predictions[i, 0]
    true_value = y_test.iloc[i]
    total_consumed += predicted
    print(f"True: {true_value:.2f} tons, Predicted: {predicted:.2f} tons")

print(f"Total Carbon Consumed for Sample Predictions: {total_consumed:.2f} tons CO2e")

# Generate a heatmap of feature correlations
correlation_matrix = data.corr()
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap="coolwarm", cbar=True)
plt.title("Feature Correlation Heatmap")
plt.show()
'''
