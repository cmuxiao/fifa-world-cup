import dash
from dash import html, dcc, callback, Input, Output
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go
import json



# Initialize the Dash app
app = dash.Dash(__name__)

# Load and prepare the data
df = pd.read_csv('world_cup.csv')

# Create a dictionary to store country codes (ISO 3-letter codes)
country_codes = {
    'Argentina': 'ARG',
    'Brazil': 'BRA',
    'Croatia': 'HRV',
    'Czechoslovakia': 'CZE',  # Using Czech Republic's code
    'England': 'GBR',
    'France': 'FRA',
    'Germany': 'DEU',
    'Hungary': 'HUN',
    'Italy': 'ITA',
    'Netherlands': 'NLD',
    'Spain': 'ESP',
    'Sweden': 'SWE',
    'Uruguay': 'URY'
}

# Add country codes to the dataframe
df['Country_Code'] = df['Winners'].map(country_codes)

# Calculate number of wins per country
wins_count = df['Winners'].value_counts().reset_index()
wins_count.columns = ['Country', 'Wins']

# Create the layout
app.layout = html.Div([
    html.H1("FIFA World Cup Dashboard", style={'textAlign': 'center', 'color': '#2c3e50'}),
    
    # Choropleth map
    html.Div([
        dcc.Graph(id='choropleth-map')
    ], style={'width': '100%', 'height': '50vh'}),
    
    # Interactive components
    html.Div([
        # Country selector
        html.Div([
            html.Label("Select a Country:"),
            dcc.Dropdown(
                id='country-dropdown',
                options=[{'label': country, 'value': country} for country in sorted(df['Winners'].unique())],
                value='Brazil',
                style={'width': '100%'}
            ),
            html.Div(id='country-stats')
        ], style={'width': '30%', 'display': 'inline-block', 'padding': '10px'}),
        
        # Year selector
        html.Div([
            html.Label("Select a Year:"),
            dcc.Dropdown(
                id='year-dropdown',
                options=[{'label': str(year), 'value': year} for year in sorted(df['Year'].unique())],
                value=2022,
                style={'width': '100%'}
            ),
            html.Div(id='year-stats')
        ], style={'width': '30%', 'display': 'inline-block', 'padding': '10px'}),
        
        # Winners list
        html.Div([
            html.Label("All World Cup Winners:"),
            html.Div(id='winners-list')
        ], style={'width': '30%', 'display': 'inline-block', 'padding': '10px'})
    ], style={'width': '100%', 'marginTop': '20px'})
])

# Callback for the choropleth map
@callback(
    Output('choropleth-map', 'figure'),
    Input('country-dropdown', 'value')
)
def update_choropleth(selected_country):
    fig = px.choropleth(
        wins_count,
        locations='Country',
        locationmode='country names',
        color='Wins',
        color_continuous_scale='Viridis',
        title='Number of World Cup Wins by Country'
    )
    fig.update_geos(showcountries=True, showcoastlines=True)
    return fig

# Callback for country statistics
@callback(
    Output('country-stats', 'children'),
    Input('country-dropdown', 'value')
)
def update_country_stats(selected_country):
    wins = len(df[df['Winners'] == selected_country])
    return html.Div([
        html.H4(f"Statistics for {selected_country}"),
        html.P(f"Number of World Cup wins: {wins}"),
        html.P("Years won:"),
        html.Ul([html.Li(year) for year in df[df['Winners'] == selected_country]['Year']])
    ])

# Callback for year statistics
@callback(
    Output('year-stats', 'children'),
    Input('year-dropdown', 'value')
)
def update_year_stats(selected_year):
    match = df[df['Year'] == selected_year].iloc[0]
    return html.Div([
        html.H4(f"World Cup {selected_year}"),
        html.P(f"Winner: {match['Winners']}"),
        html.P(f"Runner-up: {match['Runners_up']}"),
        html.P(f"Score: {match['Score']}")
    ])

# Callback for winners list
@callback(
    Output('winners-list', 'children'),
    Input('winners-list', 'id')
)
def update_winners_list(_):
    return html.Div([
        html.Ul([html.Li(f"{country} ({wins} wins)") 
                for country, wins in zip(wins_count['Country'], wins_count['Wins'])])
    ])

if __name__ == '__main__':
    app.run(debug=True)
