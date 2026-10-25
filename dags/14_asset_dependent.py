from airflow.sdk import asset
from pendulum import datetime
import os
from asset_13 import fetch_data

@asset(
    schedule=fetch_data,
    uri="/opt/airflow/logs/data/data_processed.txt",
    name="process_data"
)
def fetch_data(self):

    os.makedirs(os.path.dirname(self.uri), exist_ok=True)

    with open(self.uri, "w") as f:
        f.write(f"Data fetched Sucessfully")

    print(f"Data return to {self.uri}")

