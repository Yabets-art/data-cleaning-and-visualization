# scripts/visualize_data.py

import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set a professional visualization style
sns.set(style="whitegrid")

# Define base directories
base_dir = os.path.dirname(os.path.abspath(__file__))
plots_dir = os.path.join(base_dir, '../plots')

# Create the plots folder if it doesn't exist
if not os.path.exists(plots_dir):
    os.makedirs(plots_dir)

# Load cleaned dataset
data_path = os.path.join(base_dir, '../data/cleaned_data.csv')
data = pd.read_csv(data_path)

print("✅ Cleaned Data Loaded Successfully:\n")
print(data.head())

# Basic Info
print("\n🔹 Data Information:")
print(data.info())

# Summary Statistics
print("\n🔹 Summary Statistics:")
print(data.describe())

# -----------------------------
# Visualization Section
# -----------------------------

# 1️⃣ Age Distribution
plt.figure(figsize=(6,4))
sns.histplot(data['Age'], bins=6, kde=True, color='steelblue')
plt.title('Age Distribution of Employees')
plt.xlabel('Age')
plt.ylabel('Count')
plt.tight_layout()
plt.savefig(os.path.join(plots_dir, 'age_distribution.png'))
plt.show()

# 2️⃣ Salary Distribution
plt.figure(figsize=(6,4))
sns.histplot(data['Salary'], bins=6, kde=True, color='darkorange')
plt.title('Salary Distribution')
plt.xlabel('Salary (ETB)')
plt.ylabel('Count')
plt.tight_layout()
plt.savefig(os.path.join(plots_dir, 'salary_distribution.png'))
plt.show()

# 3️⃣ Average Salary by City
plt.figure(figsize=(7,4))
sns.barplot(x='City', y='Salary', data=data, estimator='mean', palette='viridis')
plt.title('Average Salary by City')
plt.xlabel('City')
plt.ylabel('Average Salary (ETB)')
plt.xticks(rotation=25)
plt.tight_layout()
plt.savefig(os.path.join(plots_dir, 'avg_salary_by_city.png'))
plt.show()

# 4️⃣ Gender vs Salary Comparison
plt.figure(figsize=(6,4))
sns.boxplot(x='Gender', y='Salary', data=data, palette='Set2')
plt.title('Salary Distribution by Gender')
plt.xlabel('Gender')
plt.ylabel('Salary (ETB)')
plt.tight_layout()
plt.savefig(os.path.join(plots_dir, 'salary_by_gender.png'))
plt.show()

# 5️⃣ Correlation Heatmap (numeric columns only)
numeric_data = data.select_dtypes(include='number')
plt.figure(figsize=(4,3))
sns.heatmap(numeric_data.corr(), annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Matrix')
plt.tight_layout()
plt.savefig(os.path.join(plots_dir, 'correlation_matrix.png'))
plt.show()

# 6️⃣ Salary by Age (Scatter Plot)
plt.figure(figsize=(6,4))
sns.scatterplot(x='Age', y='Salary', hue='Gender', data=data, palette='cool', s=100)
plt.title('Relationship Between Age and Salary')
plt.xlabel('Age')
plt.ylabel('Salary (ETB)')
plt.legend(title='Gender')
plt.tight_layout()
plt.savefig(os.path.join(plots_dir, 'age_vs_salary.png'))
plt.show()

print(f"\n✅ All plots saved successfully in: {plots_dir}")
