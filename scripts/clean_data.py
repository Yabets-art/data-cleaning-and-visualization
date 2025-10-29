import os
import pandas as pd

# Base directory = directory of this script
base_dir = os.path.dirname(os.path.abspath(__file__))

# Paths for reading and writing
input_path = os.path.join(base_dir, '../data/sample_data.csv')
output_path = os.path.join(base_dir, '../data/cleaned_data.csv')

# Read CSV
data = pd.read_csv(input_path)
print("Original Data:")
print(data)

# Process data here (if needed)

# Save CSV
data.to_csv(output_path, index=False)
print("\nCleaned data saved successfully!")
print("Cleaned Data:")
print(data)
