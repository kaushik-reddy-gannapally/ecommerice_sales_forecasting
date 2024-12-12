import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd
from sqlalchemy import create_engine

# Database connection
engine = create_engine("postgresql://postgres:newmonklifeisLit%4009@localhost:5433/postgres")

# Fetch forecast results
data = pd.read_sql('SELECT * FROM forecast_results', con=engine)

# Create a Dash App
app = dash.Dash(__name__)

# Create line chart
fig = px.line(data, x='date', y='predicted_revenue', title='Predicted Revenue Over Time')

# App Layout
app.layout = html.Div([
    dcc.Graph(figure=fig)
])

if __name__ == '__main__':
    app.run_server(debug=True)
