import pandas as pd


file_path = "/Users/angelren/Documents/projects/realtime-ecommerce-pipeline/data/raw/e-shop clothing 2008.csv"

df = pd.read_csv(file_path)

print("Shape:", df.shape)
print("\nColumns:")
print(df.columns.tolist())

print("\nFirst 5 rows:")
print(df.head())
