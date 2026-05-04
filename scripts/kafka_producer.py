import json
import time

import pandas as pd
from kafka import KafkaProducer


input_file = "/Users/angelren/Documents/projects/realtime-ecommerce-pipeline/data/processed/clickstream_events.csv"
topic_name = "clickstream-events"
replay_delay_seconds = 0.0001


def main():
    df = pd.read_csv(input_file)

    producer = KafkaProducer(
        bootstrap_servers="localhost:9092",
        value_serializer=lambda value: json.dumps(value).encode("utf-8"),
        key_serializer=lambda key: str(key).encode("utf-8"),
    )

    for row in df.to_dict(orient="records"):
        producer.send(topic_name, key=row["session_id"], value=row)
        time.sleep(replay_delay_seconds)

    producer.flush()
    producer.close()

    print(f"Kafka producer sent {len(df)} events to topic: {topic_name}")


if __name__ == "__main__":
    main()
