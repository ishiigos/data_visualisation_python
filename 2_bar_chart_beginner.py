# ----------------------------------------------------------------------------------------------------------------------------------------------------
# 🎯 Goal: Compare quantities across different categories. Data: Sales data for different products. 
# Visualization: Bar chart. 
# ----------------------------------------------------------------------------------------------------------------------------------------------------

import matplotlib.pyplot as plt 
import pandas as pd 

# Sample data 

data = {'Product': ['A', 'B', 'C', 'D', 'E'], 
'Sales': [150, 200, 120, 180, 250]} 
df = pd.DataFrame(data) 

# Create the bar chart 

plt.figure(figsize=(8, 6)) 
plt.bar(df['Product'], df['Sales'], color=['lightcoral', 'lightgreen', 
'lightblue', 'gold', 'plum']) 
plt.title('Total Sales by Product') 
plt.xlabel('Product') 
plt.ylabel('Sales (Units)') 
plt.grid(axis='y', linestyle='--', alpha=0.7) 
plt.show() 