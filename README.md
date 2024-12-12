E-commerce Sales Forecasting Project
Overview
This project aims to predict future sales revenue for an e-commerce platform using historical data. It integrates several components of data management in data science, including:

Database Management (PostgreSQL): Storing and managing raw and processed sales data.
Data Preprocessing (ETL): Cleaning and transforming the input data.
Machine Learning (Random Forest): Training a predictive model to forecast sales.
Visualization (Dash Dashboard): Providing an interactive interface to visualize both historical and predicted sales.
Features
Robust Database Schema: Separate tables for sales_data, product_info, and forecast_results.
ETL Pipeline: Scripts that clean, normalize, and load data into the database.
Predictive Modeling: A Random Forest model trained to forecast future revenue.
Interactive Dashboard: A user-friendly web app built with Dash to explore trends and predictions.
Directory Structure
bash
Copy code
ecommerce_sales_forecasting/
├─ data/
│  ├─ raw_sales_data.csv        # Original raw sales dataset
│  ├─ processed_X_train.csv     # Processed training data
│  ├─ processed_y_train.csv     # Processed training labels
│  ├─ processed_X_test.csv      # Processed test data
│  ├─ processed_y_test.csv      # Processed test labels
│
├─ models/
│  ├─ random_forest.pkl         # Trained Random Forest model
│
├─ scripts/
│  ├─ setup_database.py         # Sets up the PostgreSQL schema
│  ├─ etl_pipeline.py           # Loads raw data into database, cleans it
│  ├─ preprocess_data.py        # Preprocesses data and splits into train/test
│  ├─ train_model.py            # Trains the Random Forest model
│  ├─ automate_predictions.py   # Fetches new data, makes predictions, stores results
│  ├─ simulate_data_ingestion.py# Simulates inserting new sales rows in real-time
│  ├─ visualize_dashboard.py    # Runs the Dash dashboard for visualization
│
├─ logs/
│  ├─ etl_log.txt               # ETL pipeline logs
│
├─ requirements.txt             # Python dependencies
├─ README.md                    # This readme file
└─ ...
Getting Started
Prerequisites
Python 3.8+
PostgreSQL 13+
Python Libraries: Listed in requirements.txt, including:
pandas
numpy
sqlalchemy
psycopg2
scikit-learn
dash
plotly
Installation
Set Up Virtual Environment (recommended):
bash
Copy code
python3 -m venv venv
source venv/bin/activate
Install Dependencies:
bash
Copy code
pip install -r requirements.txt
Configure Database:
Ensure PostgreSQL is running.
Update database connection strings in the scripts with your credentials.
Initializing the Database
bash
Copy code
python scripts/setup_database.py
This will create the necessary tables (sales_data, product_info, forecast_results).

Running the ETL Pipeline
bash
Copy code
python scripts/etl_pipeline.py
Loads raw data from data/raw_sales_data.csv into the sales_data table and performs initial cleaning.

Preprocessing Data
bash
Copy code
python scripts/preprocess_data.py
Prepares training and testing sets, and saves them in data/ directory.

Training the Model
bash
Copy code
python scripts/train_model.py
Trains the Random Forest model and saves the trained model in models/random_forest.pkl.

Automating Predictions
bash
Copy code
python scripts/automate_predictions.py
Fetches recent data from the database, predicts future sales, and stores results in forecast_results table.

Simulating Real-Time Data Ingestion (Optional)
bash
Copy code
python scripts/simulate_data_ingestion.py
Inserts new rows into sales_data at intervals to simulate a live stream of data.

Running the Dashboard
bash
Copy code
python scripts/visualize_dashboard.py
Access the dashboard in your browser at http://127.0.0.1:8050/ to explore sales trends and forecasts interactively.

Results and Analysis
Model Performance: The Random Forest model achieved an RMSE of approximately 540.6. This indicates that on average predictions are off by about 540.6 units of revenue.
Insights: Certain seasonal patterns were identified; sales tend to vary by month and product category.
Future Work
Consider integrating additional features or external datasets (e.g., promotional events or holidays) to improve model accuracy.
Explore more advanced models like Gradient Boosting or Neural Networks.
Move from simulated real-time ingestion to a live API-based data feed.
