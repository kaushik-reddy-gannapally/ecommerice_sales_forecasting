import pandas as pd
import joblib
from sqlalchemy import create_engine

# Load the model
model = joblib.load('models/random_forest.pkl')

# Database connection
engine = create_engine("postgresql://postgres:newmonklifeisLit%4009@localhost:5433/postgres")

# Fetch new data
new_data = pd.read_sql(
    'SELECT * FROM sales_data',
    con=engine
)

# Debugging: Check fetched data
print(new_data)

if new_data.empty:
    print("No records found in sales_data matching the date criteria.")
    exit()

# Preprocess new data
new_data['month'] = pd.to_datetime(new_data['date']).dt.month
new_data['year'] = pd.to_datetime(new_data['date']).dt.year
X_new = new_data[['month', 'year', 'quantity_sold']]

# Check the shape of the feature matrix
print("Feature matrix (X_new):")
print(X_new)

if X_new.empty:
    print("Feature matrix is empty. Check the sales_data table for missing or invalid data.")
    exit()

# Make predictions
predictions = model.predict(X_new)
new_data['predicted_revenue'] = predictions

# Save predictions to the database
new_data[['date', 'product_id', 'predicted_revenue']].to_sql(
    'forecast_results', con=engine, if_exists='append', index=False
)

print("Predictions completed and stored successfully!")