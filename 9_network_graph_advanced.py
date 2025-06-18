# ----------------------------------------------------------------------------------------------------------------------------------------
# Level: Advanced
# 🎯 Goal: Visualize relationships between entities as nodes and edges. 
# Dataset: Synthetic social network data. 
# Visualization: Force-directed network graph. 
# ----------------------------------------------------------------------------------------------------------------------------------------

import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

# Sample synthetic graph

np.random.seed(42)
G = nx.Graph()

# Generate synthetic "biological" node names

nodes = [f"Gene{chr(65 + i)}{j}" for i in range(5) for j in range(1, 6)]  # GeneA1–GeneE5
G.add_nodes_from(nodes)

# Randomly connect nodes

for _ in range(40):
    n1, n2 = np.random.choice(nodes, 2, replace=False)
    G.add_edge(n1, n2, weight=np.random.randint(1, 10))

# Plot force-directed graph

plt.figure(figsize=(12, 8))
pos = nx.spring_layout(G, seed=42)  # Force-directed layout
edges = G.edges(data=True)
weights = [edge[2]['weight'] for edge in edges]

nx.draw_networkx_nodes(G, pos, node_color='skyblue', node_size=500)
nx.draw_networkx_edges(G, pos, width=weights, alpha=0.7)
nx.draw_networkx_labels(G, pos, font_size=10, font_weight='bold')

plt.title("Force-Directed Network Graph: Gene Interactions")
plt.axis('off')
plt.tight_layout()
plt.show()

