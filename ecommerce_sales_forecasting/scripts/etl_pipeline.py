import pandas as pd
from sqlalchemy import create_engine

# Database connection
engine = create_engine("postgresql://postgres:newmonklifeisLit%4009@localhost:5433/postgres")

try:
    with engine.connect() as conn:
        print("Database connection successful!")
except Exception as e:
    print(f"Database connection failed: {e}")


# Load dataset
data = pd.read_csv('data/retail_sales_dataset.csv')

# Map Product Category to Product ID
product_mapping = {
    'Beauty': 1,
    'Clothing': 2,
    'Electronics': 3
}

# Prepare sales_data table
sales_data = data.copy()
sales_data['product_id'] = sales_data['Product Category'].map(product_mapping)
sales_data['store_id'] = 1  # Dummy value since store_id is not provided
sales_data = sales_data.rename(columns={
    'Date': 'date',
    'Quantity': 'quantity_sold',
    'Total Amount': 'revenue'
})
sales_data = sales_data[['date', 'product_id', 'quantity_sold', 'revenue', 'store_id']]

# Prepare product_info table
product_info = pd.DataFrame({
    'product_id': [1, 2, 3],
    'product_name': ['Beauty', 'Clothing', 'Electronics'],
    'category': ['Personal Care', 'Apparel', 'Gadgets'],
    'price': [50, 300, 500],  # Example average prices
    'stock_level': [100, 200, 150]  # Example stock levels
})

# Load data into PostgreSQL
sales_data.to_sql('sales_data', con=engine, if_exists='replace', index=False)
product_info.to_sql('product_info', con=engine, if_exists='replace', index=False)

print("ETL pipeline executed successfully!")