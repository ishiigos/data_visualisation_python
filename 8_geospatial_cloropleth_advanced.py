# ----------------------------------------------------------------------------------------------------------------------------------------
# Level: Advanced
# 🎯 Goal: Visualize geographical data, typically showing different values by coloring regions on a map. Interactive elements enhance exploration.
# Dataset: US State unemployment data (synthetic for simplicity) and a GeoJSON file for state boundaries.
# Note: Used basic folium approach and a public GeoJSON. 
# ----------------------------------------------------------------------------------------------------------------------------------------

import folium 
import pandas as pd 
import json 

# Synthetic US State Unemployment Data 

data_unemployment = { 
'State': ['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL', 
'GA', 'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD', 
'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 
'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 
'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY'], 
'Unemployment_Rate': [4.5, 6.2, 5.1, 4.8, 7.5, 3.9, 5.8, 4.7, 6.5, 
5.3, 4.0, 3.5, 6.8, 5.5, 3.2, 3.1, 5.9, 6.1, 4.3, 4.6, 5.2, 7.0, 3.8, 
6.0, 4.9, 3.3, 2.9, 8.0, 3.0, 6.3, 6.7, 7.1, 5.6, 2.8, 6.4, 4.4, 5.7, 
6.6, 7.2, 5.0, 2.7, 5.4, 6.9, 3.4, 3.6, 4.2, 6.0, 7.3, 4.1, 3.7] 
} 
df_unemployment = pd.DataFrame(data_unemployment) 
 
# Load a GeoJSON file for US states (you'll need to download this or use a URL) 
# Example public URL for US states GeoJSON: 
# 'https://raw.githubusercontent.com/python-visualization/folium-example-data/main/us_states.json' 
# For demonstration, let's assume you have it locally or use the direct URL. 
# If you download it, save it as 'us_states.json' in your working directory. 

try: 
    with open('us_states.json', 'r') as f: 
        geo_data = json.load(f) 
except FileNotFoundError: 
    print("us_states.json not found. Attempting to download from GitHub...") 
    import requests 
    url = 'https://raw.githubusercontent.com/python-visualization/folium-example-data/main/us_states.json' 
    response = requests.get(url) 
    geo_data = response.json() 
    with open('us_states.json', 'w') as f: 
        json.dump(geo_data, f) 
    print("us_states.json downloaded.") 
 
# Create a Folium map centered on the US 

m = folium.Map(location=[39.8283, -98.5795], zoom_start=4) 
 
# Add the choropleth layer 

folium.Choropleth( 
    geo_data=geo_data, 
    name='choropleth', 
    data=df_unemployment, 
    columns=['State', 'Unemployment_Rate'], 
    key_on='feature.id', # The key in your GeoJSON that matches your 'State' column 
    fill_color='YlOrRd', 
    fill_opacity=0.7, 
    line_opacity=0.2, 
    legend_name='Unemployment Rate (%)', 
    highlight=True # Highlight on hover 
).add_to(m) 
 
# Add tooltips for interactivity 

style_function = lambda x: {'fillColor': '#ffffff', 
                            'color': 'black', 
                            'fillOpacity': 0.1, 
                            'weight': 0.1} 
highlight_function = lambda x: {'fillColor': '#000000', 
                                'color': 'black', 
                                'fillOpacity': 0.50, 
                                'weight': 0.1} 
NIL = folium.features.GeoJson( 
    geo_data, 
    style_function=style_function, 
    control=False, 
    highlight_function=highlight_function, 
    tooltip=folium.features.GeoJsonTooltip( 
        fields=['name'], 
        aliases=['State:'], 
        localize=True, 
        sticky=False, 
        labels=True, 
        style="background-color: #F0EFE9; border: 2px solid black; border-radius: 3px; box-shadow: 3px;" 
    ) 
) 
m.add_child(NIL) 
m.keep_in_front(NIL) 
 
folium.LayerControl().add_to(m) 

import webbrowser
import os

# Save the map to an HTML file
map_path = "us_unemployment_map.html"
m.save(map_path)
print(f"Interactive map saved to {map_path}")

# Open the saved HTML in the default web browser
webbrowser.open("file://" + os.path.realpath(map_path))