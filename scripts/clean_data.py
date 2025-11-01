import os
import pandas as pd

# ===============================================================
# STEP 1: SET UP PATHS
# ===============================================================
# Define the base directory (where this script is located)
base_dir = os.path.dirname(os.path.abspath(__file__))

# Define input and output paths relative to the project structure
input_path = os.path.join(base_dir, '../data/sample_data.csv')
output_path = os.path.join(base_dir, '../data/cleaned_data.csv')

# ===============================================================
# STEP 2: READ RAW DATA
# ===============================================================
try:
    data = pd.read_csv(input_path)
    print("✅ Raw data loaded successfully!\n")
except FileNotFoundError:
    print("❌ Error: The file sample_data.csv was not found.")
    exit()

print("📊 Original (Raw) Data Preview:")
print(data.head(), "\n")  # Show first 5 rows

# ===============================================================
# STEP 3: DATA CLEANING PROCESS (Enhanced)
# ===============================================================

# 1️⃣ Remove duplicate records (case-insensitive for 'Name')
data['Name_lower'] = data['Name'].str.lower()
data = data.drop_duplicates(subset=['Name_lower'], keep='first')
data.drop(columns=['Name_lower'], inplace=True)

# 2️⃣ Handle missing values
for col in data.columns:
    if data[col].dtype in ['int64', 'float64']:
        data[col].fillna(data[col].mean(), inplace=True)
    else:
        data[col].fillna('Unknown', inplace=True)

# 3️⃣ Standardize text formatting
if 'Gender' in data.columns:
    data['Gender'] = data['Gender'].str.title().replace({
        'M': 'Male',
        'F': 'Female'
    })

if 'City' in data.columns:
    # Convert all city names to proper title case
    data['City'] = data['City'].str.title()

# 4️⃣ Remove invalid or unrealistic numeric entries
if 'Salary' in data.columns:
    data = data[data['Salary'] > 0]

# ===============================================================
# STEP 4: SAVE CLEANED DATA
# ===============================================================
data.to_csv(output_path, index=False)

print("✅ Cleaned data saved successfully!")
print(f"📁 File location: {output_path}\n")

# ===============================================================
# STEP 5: FINAL VERIFICATION
# ===============================================================
print("📈 Cleaned Data Preview:")
print(data.head())

print("\n🎯 Data cleaning process completed successfully!")
