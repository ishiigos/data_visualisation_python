# ---------------------------------------------------------------------------------------------------------------------------------
# Level: Intermediate
# 🎯 Goal: Visualize hierarchical data using nested rectangles, where the size of each rectangle is proportional to its value.
# Dataset: Synthetic data representing product categories and sales.
# ---------------------------------------------------------------------------------------------------------------------------------

import matplotlib.pyplot as plt
import pandas as pd
import squarify  # pip install squarify
import numpy as np

# Synthetic hierarchical data: Gene Clusters and Expression Levels
np.random.seed(42)

categories = ['Cluster A', 'Cluster B', 'Cluster C', 'Cluster D', 'Cluster E']
subcategories = [f"{cat.split()[1]}{i}" for cat in categories for i in range(1, 11)]  # A1–A10, ..., E1–E10

sales = np.random.randint(50, 500, size=len(subcategories))  # Expression values

df_tree = pd.DataFrame({
    'category': [cat for cat in categories for _ in range(10)],
    'subcategory': subcategories,
    'sales': sales
})

# Aggregate if needed
df_agg = df_tree.groupby('subcategory')['sales'].sum().reset_index()
labels = df_agg.apply(lambda x: f"{x['subcategory']}\n({x['sales']})", axis=1)
sizes = df_agg['sales'].tolist()

# Plot
plt.figure(figsize=(16, 10))
squarify.plot(
    sizes=sizes,
    label=labels,
    alpha=0.85,
    color=plt.cm.viridis(np.linspace(0.1, 0.9, len(sizes)))
)
plt.title('Synthetic Expression Levels by Subcategory (Treemap)', fontsize=18)
plt.axis('off')
plt.tight_layout()
plt.show()