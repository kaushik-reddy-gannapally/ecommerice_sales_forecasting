import psycopg2

# Database connection
conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="newmonklifeisLit@09",
    host="localhost",
    port="5433"
)
cursor = conn.cursor()

# SQL commands to create tables
create_tables_sql = """
CREATE TABLE IF NOT EXISTS sales_data (
    sale_id SERIAL PRIMARY KEY,
    date DATE NOT NULL,
    product_id INT NOT NULL,
    quantity_sold INT NOT NULL,
    revenue NUMERIC(10, 2),
    store_id INT NOT NULL
);

CREATE TABLE IF NOT EXISTS product_info (
    product_id SERIAL PRIMARY KEY,
    product_name VARCHAR(255),
    category VARCHAR(255),
    price NUMERIC(10, 2),
    stock_level INT
);

CREATE TABLE IF NOT EXISTS inventory_logs (
    log_id SERIAL PRIMARY KEY,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    product_id INT NOT NULL,
    stock_change INT,
    location VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS forecast_results (
    forecast_id SERIAL PRIMARY KEY,
    date DATE NOT NULL,
    product_id INT NOT NULL,
    predicted_revenue NUMERIC(10, 2)
);
"""

# Execute the SQL commands
cursor.execute(create_tables_sql)
conn.commit()

# Close connection
cursor.close()
conn.close()
print("Database setup completed.")
