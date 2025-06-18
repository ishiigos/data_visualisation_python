# -------------------------------------------------------------------------------------------------------------------------------
# Level: Intermediate
# 🎯 Goal: Show the distribution of a numerical variable across multiple categories, with an additional categorical breakdown.
# Dataset: Palmer Penguins (built-in in Seaborn) - a classic for demonstrating various plot types.
# -------------------------------------------------------------------------------------------------------------------------------
 
import seaborn as sns 
import matplotlib.pyplot as plt 

# Load the Palmer Penguins dataset 

penguins = sns.load_dataset("penguins") 
plt.figure(figsize=(10, 7)) 

sns.violinplot( 
data=penguins, 
x="species", 
y="bill_length_mm", 
hue="sex", 
palette="viridis", 
inner="quartile" # Shows quartiles inside the violins 
) 

plt.title('Bill Length Distribution by Species and Sex (Violin Plot)', 
fontsize=16) 
plt.xlabel('Species', fontsize=12) 
plt.ylabel('Bill Length (mm)', fontsize=12) 
plt.legend(title='Sex') 
plt.grid(axis='y', linestyle='--', alpha=0.7) 
plt.show() 