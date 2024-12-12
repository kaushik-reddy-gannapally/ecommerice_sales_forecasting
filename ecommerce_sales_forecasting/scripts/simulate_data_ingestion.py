import time
from sqlalchemy import create_engine, text

# Database connection
engine = create_engine("postgresql://postgres:newmonklifeisLit%4009@localhost:5433/postgres")

# Sample data
rows = [
    ('2024-12-15', 1, 5, 100.0, 1),
    ('2024-12-16', 2, 10, 500.0, 1),
    ('2024-12-17', 3, 2, 200.0, 1)
]

# Insert rows periodically
with engine.connect() as conn:
    for row in rows:
        conn.execute(
            text("INSERT INTO sales_data (date, product_id, quantity_sold, revenue, store_id) VALUES (:date, :product_id, :quantity_sold, :revenue, :store_id)"),
            {
                'date': row[0],
                'product_id': row[1],
                'quantity_sold': row[2],
                'revenue': row[3],
                'store_id': row[4],
            }
        )
        print(f"Inserted: {row}")
        time.sleep(5)  # Simulate real-time data ingestion
