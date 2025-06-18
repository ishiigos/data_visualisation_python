import plotly.express as px
import pandas as pd

# --------------------------------------------
# 🎯 GOAL: Visualize GDP, life expectancy, and population
# using an interactive bubble chart.
# --------------------------------------------

def load_gapminder_data():
    """Try loading the built-in Gapminder dataset, else use dummy fallback."""
    try:
        return px.data.gapminder()
    except Exception:
        print("Gapminder dataset not found. Using dummy data.")
        dummy_data = {
            'country': ['A', 'B', 'C', 'D', 'E', 'F'],
            'continent': ['Asia', 'Europe', 'Asia', 'Africa', 'Europe', 'Africa'],
            'year': [2007] * 6,
            'lifeExp': [70, 75, 65, 55, 80, 60],
            'pop': [10_000_000, 5_000_000, 20_000_000, 30_000_000, 8_000_000, 15_000_000],
            'gdpPercap': [10000, 25000, 5000, 2000, 40000, 3000]
        }
        return pd.DataFrame(dummy_data)

# Load data
df = load_gapminder_data()

# Filter for a single year (optional: here using 2007 for clarity)
df_latest = df[df["year"] == 2007]

# --------------------------------------------
# 📊 Create interactive bubble chart
# --------------------------------------------
fig = px.scatter(
    df_latest,
    x="gdpPercap",
    y="lifeExp",
    size="pop",
    color="continent",
    hover_name="country",
    log_x=True,
    size_max=60,
    title="🌍 Life Expectancy vs GDP Per Capita (2007)"
)

html_file = "bubble_chart.html"
fig.write_html(html_file)

import webbrowser
import os

webbrowser.open("file://" + os.path.realpath(html_file))
