# -------------------------------------------------------------------------------------------------------
# 🎯 Goal: Visualize the relationship between two continuous variables. Data: Simple synthetic data. 
# Visualization: Scatter plot. 
# -------------------------------------------------------------------------------------------------------

import matplotlib.pyplot as plt 
import numpy as np 

# Generate some data 

np.random.seed(42) 
x = np.random.rand(50) * 10 
y = 2 * x + np.random.randn(50) * 2 

# Create the scatter plot 

plt.figure(figsize=(8, 6)) 
plt.scatter(x, y, color='skyblue', alpha=0.7) 
plt.title('Scatter Plot of X vs Y') 
plt.xlabel('X-axis') 
plt.ylabel('Y-axis') 
plt.grid(True, linestyle='--', alpha=0.6) 
plt.show() 
