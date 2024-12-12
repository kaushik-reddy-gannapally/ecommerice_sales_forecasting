import pandas as pd
from sqlalchemy import create_engine  # Import create_engine for database connection
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Database connection
engine = create_engine("postgresql://postgres:newmonklifeisLit%4009@localhost:5433/postgres")

# Load data from PostgreSQL
data = pd.read_sql('SELECT * FROM sales_data', con=engine)

# Feature Engineering
data['month'] = pd.to_datetime(data['date']).dt.month
data['year'] = pd.to_datetime(data['date']).dt.year

# Split features and target
X = data[['month', 'year', 'quantity_sold']]
y = data['revenue']

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Standardize features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Save preprocessed data
X_train.to_csv('data/processed_X_train.csv', index=False)
y_train.to_csv('data/processed_y_train.csv', index=False)
X_test.to_csv('data/processed_X_test.csv', index=False)
y_test.to_csv('data/processed_y_test.csv', index=False)

print("Data preprocessing completed and saved to CSV files.")