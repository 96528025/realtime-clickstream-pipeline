import pandas as pd


input_file = "/Users/angelren/Documents/projects/realtime-ecommerce-pipeline/data/raw/e-shop clothing 2008.csv"
output_file = "/Users/angelren/Documents/projects/realtime-ecommerce-pipeline/data/processed/clickstream_events.csv"

df = pd.read_csv(input_file, sep=";")

df = df.rename(
    columns={
        "session ID": "session_id",
        "page 1 (main category)": "main_category",
        "page 2 (clothing model)": "clothing_model",
        "model photography": "model_photography",
        "price 2": "price_band",
    }
)

df["event_time"] = pd.to_datetime(
    df[["year", "month", "day"]]
) + pd.to_timedelta(df["order"], unit="s")

df = df.sort_values(["event_time", "session_id", "order"]).reset_index(drop=True)
df["event_id"] = df.index + 1
df["event_type"] = "page_view"

ordered_columns = [
    "event_id",
    "event_time",
    "event_type",
    "session_id",
    "country",
    "main_category",
    "clothing_model",
    "colour",
    "location",
    "model_photography",
    "price",
    "price_band",
    "page",
    "year",
    "month",
    "day",
    "order",
]

df = df[ordered_columns]
df.to_csv(output_file, index=False)

print(f"Prepared events saved to: {output_file}")
print(f"Shape: {df.shape}")
print("\nColumns:")
print(df.columns.tolist())
print("\nFirst 5 rows:")
print(df.head())
