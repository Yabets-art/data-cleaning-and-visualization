# scripts/visualize_data.py

import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set plot style
sns.set(style="whitegrid")

# Create directory for plots if it doesn't exist
plots_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../plots')
if not os.path.exists(plots_dir):
    os.makedirs(plots_dir)

# Load cleaned CSV
data_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../data/cleaned_data.csv')
data = pd.read_csv(data_path)

print("Data Loaded Successfully:\n")
print(data.head())

# Basic Info
print("\nData Info:")
print(data.info())

# Summary Statistics
print("\nSummary Statistics:")
print(data.describe())

# -----------------------------
# Visualization Section
# -----------------------------

# 1. Age Distribution
plt.figure(figsize=(6,4))
sns.histplot(data['Age'], bins=5, kde=True, color='skyblue')
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Count')
age_plot_path = os.path.join(plots_dir, 'age_distribution.png')
plt.savefig(age_plot_path)
plt.show()

# 2. Score Distribution
plt.figure(figsize=(6,4))
sns.histplot(data['Score'], bins=5, kde=True, color='orange')
plt.title('Score Distribution')
plt.xlabel('Score')
plt.ylabel('Count')
score_plot_path = os.path.join(plots_dir, 'score_distribution.png')
plt.savefig(score_plot_path)
plt.show()

# 3. Scores by Name (Bar Chart)
plt.figure(figsize=(6,4))
sns.barplot(x='Name', y='Score', data=data, palette='viridis', hue=None, dodge=False)
plt.title('Scores by Name')
plt.xlabel('Name')
plt.ylabel('Score')
bar_plot_path = os.path.join(plots_dir, 'scores_by_name.png')
plt.savefig(bar_plot_path)
plt.show()

# 4. Correlation Heatmap (Numeric columns only)
numeric_data = data.select_dtypes(include='number')
plt.figure(figsize=(4,3))
sns.heatmap(numeric_data.corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
corr_plot_path = os.path.join(plots_dir, 'correlation_matrix.png')
plt.savefig(corr_plot_path)
plt.show()

print("\nAll plots saved to:", plots_dir)
