"""Goal: Visualize the correlation between multiple numerical variables. Data: Iris dataset (built-in 
in seaborn). Visualization: Heatmap. 
"""

import seaborn as sns 
import matplotlib.pyplot as plt 
import pandas as pd 

# Load the Iris dataset 

iris = sns.load_dataset('iris') 

# Calculate the correlation matrix 

correlation_matrix = iris.drop(columns=['species']).corr() 
 
# Create the heatmap 

plt.figure(figsize=(8, 7)) 
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', 
fmt=".2f", linewidths=.5) 
plt.title('Correlation Matrix of Iris Features') 
plt.show()