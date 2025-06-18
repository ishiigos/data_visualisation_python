# ----------------------------------------------------------------------------------------------------------------------------------------
# Level: Advanced
# 🎯 Goal: Goal: Create a simple interactive web application with linked plots. This introduces the concept of dashboards. 
# Dataset: Tips dataset (built-in in Plotly Express). 
# Note: Dash requires running a small web server. Save this as app.py and run python app.py from your terminal. 
# ----------------------------------------------------------------------------------------------------------------------------------------

from dash import Dash, html, dcc, callback, Output, Input 
import plotly.express as px 
import pandas as pd 

# Load the tips dataset 

df_tips = px.data.tips()

# Initialize the Dash app 

app = Dash(__name__) 
 
# Define the layout of the app 

app.layout = html.Div([ 
    html.H1(children='Tips Analysis Dashboard', style={'textAlign':'center'}), 
 
    html.Div([ 
        html.Div([ 
            html.Label('Select Day:'), 
            dcc.Dropdown( 
                id='day-dropdown', 
                options=[{'label': i, 'value': i} for i in df_tips['day'].unique()], 
                value='Fri', # Default value 
                clearable=False 
            ) 
        ], style={'width': '48%', 'display': 'inline-block', 'padding': '10px'}), 
 
        html.Div([ 
            html.Label('Select Time:'), 
            dcc.RadioItems( 
                id='time-radio', 
                options=[{'label': i, 'value': i} for i in df_tips['time'].unique()], 
                value='Dinner', # Default value 
                inline=True 
            ) 
        ], style={'width': '48%', 'display': 'inline-block', 'padding': '10px'}), 
    ], style={'display': 'flex', 'justify-content': 'space-around'}), 
 
    html.Div([ 
        html.Div([dcc.Graph(id='scatter-plot')], style={'width': '49%', 'display': 'inline-block', 'vertical-align': 'top'}), 
        html.Div([dcc.Graph(id='bar-chart')], style={'width': '49%', 'display': 'inline-block', 'vertical-align': 'top'}) 
    ], style={'display': 'flex', 'justify-content': 'space-around'}) 
]) 
 
# Define callbacks to update graphs based on selections 

@callback( 
    Output('scatter-plot', 'figure'), 
    Output('bar-chart', 'figure'), 
    Input('day-dropdown', 'value'), 
    Input('time-radio', 'value') 
) 

def update_graph(selected_day, selected_time): 
    filtered_df = df_tips[(df_tips['day'] == selected_day) & (df_tips['time'] == selected_time)] 
 
    scatter_fig = px.scatter( 
        filtered_df, 
        x="total_bill", 
        y="tip", 
        color="sex", 
        hover_data=["smoker", "size"], 
        title=f'Total Bill vs. Tip on {selected_day} {selected_time}' 
    ) 
    scatter_fig.update_layout(margin={"t":40, "b":0, "l":0, "r":0}) 
 
    bar_fig = px.bar( 
        filtered_df, 
        x="size", 
        y="tip", 
        color="sex", 
        barmode="group", 
        title=f'Tip Amount by Party Size on {selected_day} {selected_time}' 
    ) 
    bar_fig.update_layout(margin={"t":40, "b":0, "l":0, "r":0}) 
 
    return scatter_fig, bar_fig 
 
# Run the app 

if __name__ == '__main__': 
    app.run(debug=True)
