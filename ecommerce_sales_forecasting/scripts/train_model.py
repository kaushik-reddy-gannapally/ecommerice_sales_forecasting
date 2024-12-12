import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import joblib
from math import sqrt

# Load preprocessed data
X_train = pd.read_csv('data/processed_X_train.csv')
y_train = pd.read_csv('data/processed_y_train.csv')
X_test = pd.read_csv('data/processed_X_test.csv')
y_test = pd.read_csv('data/processed_y_test.csv')

# Train model
model = RandomForestRegressor(random_state=42)
model.fit(X_train, y_train.values.ravel())

# Predict and evaluate
y_pred = model.predict(X_test)
rmse = sqrt(mean_squared_error(y_test, y_pred))  # Compute RMSE explicitly
print(f"RMSE: {rmse}")

# Save model
joblib.dump(model, 'models/random_forest.pkl')
print("Model training completed and saved.")