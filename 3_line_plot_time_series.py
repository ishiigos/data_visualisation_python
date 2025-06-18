# ----------------------------------------------------------------------------------------------------------------------------------------------------
# 🎯 Goal: Show trends over time. Data: Daily stock prices. Visualization: Line plot. 
# ----------------------------------------------------------------------------------------------------------------------------------------------------

import matplotlib.pyplot as plt 
import pandas as pd 
import numpy as np 

# Generate synthetic time series data 

dates = pd.date_range(start='2024-01-01', periods=100, freq='D') 
stock_prices = np.random.randn(100).cumsum() + 100 
df_time = pd.DataFrame({'Date': dates, 'Price': stock_prices}) 

# Create the line plot 

plt.figure(figsize=(12, 6)) 
plt.plot(df_time['Date'], df_time['Price'], color='teal', linewidth=2) 
plt.title('Daily Stock Price Trend') 
plt.xlabel('Date') 
plt.ylabel('Price') 
plt.grid(True, linestyle='--', alpha=0.6) 
plt.xticks(rotation=45) 
plt.tight_layout() 
plt.show() 