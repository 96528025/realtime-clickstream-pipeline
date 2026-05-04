from pathlib import Path
from urllib.request import urlretrieve
from zipfile import ZipFile


output_dir = Path("/Users/angelren/Documents/projects/realtime-ecommerce-pipeline/data/raw")
zip_file = output_dir / "clickstream_online_shopping.zip"
download_url = "https://cdn.uci-ics-mlr-prod.aws.uci.edu/553/clickstream%2Bdata%2Bfor%2Bonline%2Bshopping.zip"

output_dir.mkdir(parents=True, exist_ok=True)
urlretrieve(download_url, zip_file)

with ZipFile(zip_file, "r") as zip_ref:
    zip_ref.extractall(output_dir)

print(f"Dataset zip saved to: {zip_file}")
print(f"Extracted files to: {output_dir}")
