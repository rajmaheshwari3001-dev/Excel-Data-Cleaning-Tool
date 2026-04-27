import pandas as pd

file = input("Enter file name (with .csv): ")
df = pd.read_csv(file)

# Remove duplicates
df = df.drop_duplicates()

# Handle missing values safely
if "Age" in df.columns:
    df["Age"] = df["Age"].fillna(0)

if "City" in df.columns:
    df["City"] = df["City"].fillna("Unknown")

if "Salary" in df.columns:
    df["Salary"] = df["Salary"].fillna(0)

# Save cleaned file
df.to_csv("clean_data.csv", index=False)

print("✅ Data cleaned successfully!")
print("Total rows:", len(df))