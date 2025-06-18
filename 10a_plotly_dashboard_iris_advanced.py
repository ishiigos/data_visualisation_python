# --------------------------------------------------------------------------------------------------------------------------------------
# Level: Advanced
# 🎯 Goal: Goal: Create a simple interactive web application with linked plots. This introduces the concept of dashboards. 
# Dataset: Tips dataset (built-in in Plotly Express). 
# Note: Dash requires running a small web server. Save this as app.py and run python app.py from your terminal. 
# --------------------------------------------------------------------------------------------------------------------------------------

from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd

# Load the iris dataset

df_iris = px.data.iris()

# Initialize the Dash app

app = Dash(__name__)

# Define the layout

app.layout = html.Div([
    html.H1("🌸 Iris Flower Dataset Explorer", style={'textAlign': 'center'}),

    html.Div([
        html.Label('Select Iris Species:'),
        dcc.Dropdown(
            id='species-dropdown',
            options=[{'label': species, 'value': species} for species in df_iris['species'].unique()],
            value='setosa',
            clearable=False
        )
    ], style={'width': '40%', 'margin': 'auto', 'padding': '20px'}),

    html.Div([
        html.Div([dcc.Graph(id='sepal-plot')], style={'width': '48%', 'display': 'inline-block'}),
        html.Div([dcc.Graph(id='petal-plot')], style={'width': '48%', 'display': 'inline-block'})
    ], style={'display': 'flex', 'justify-content': 'space-around'})
])

# Callback to update plots

@callback(
    Output('sepal-plot', 'figure'),
    Output('petal-plot', 'figure'),
    Input('species-dropdown', 'value')
)

def update_graphs(selected_species):
    filtered_df = df_iris[df_iris['species'] == selected_species]

    sepal_fig = px.scatter(
        filtered_df,
        x='sepal_length',
        y='sepal_width',
        color='species',
        title=f'Sepal Length vs Width ({selected_species.capitalize()})'
    )

    sepal_fig.update_layout(margin={"t": 40, "b": 0, "l": 0, "r": 0})

    petal_fig = px.scatter(
        filtered_df,
        x='petal_length',
        y='petal_width',
        color='species',
        title=f'Petal Length vs Width ({selected_species.capitalize()})'
    )

    petal_fig.update_layout(margin={"t": 40, "b": 0, "l": 0, "r": 0})

    return sepal_fig, petal_fig

# Run the app

if __name__ == '__main__':
    app.run(debug=True)