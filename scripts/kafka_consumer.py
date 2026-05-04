import json
import sqlite3
from collections import defaultdict

from kafka import KafkaConsumer


db_file = "/Users/angelren/Documents/projects/realtime-ecommerce-pipeline/data/processed/realtime_clickstream_kafka.db"
topic_name = "clickstream-events"


def create_tables(connection):
    cursor = connection.cursor()
    cursor.execute("DROP TABLE IF EXISTS raw_events")
    cursor.execute("DROP TABLE IF EXISTS stream_metrics")
    cursor.execute(
        """
        CREATE TABLE raw_events (
            event_id INTEGER PRIMARY KEY,
            event_time TEXT,
            event_type TEXT,
            session_id INTEGER,
            country INTEGER,
            main_category INTEGER,
            clothing_model TEXT,
            colour INTEGER,
            location INTEGER,
            model_photography INTEGER,
            price INTEGER,
            price_band INTEGER,
            page INTEGER,
            year INTEGER,
            month INTEGER,
            day INTEGER,
            event_order INTEGER
        )
        """
    )
    cursor.execute(
        """
        CREATE TABLE stream_metrics (
            metric_name TEXT,
            dimension TEXT,
            metric_value INTEGER
        )
        """
    )
    connection.commit()


def main():
    connection = sqlite3.connect(db_file)
    create_tables(connection)
    cursor = connection.cursor()

    consumer = KafkaConsumer(
        topic_name,
        bootstrap_servers="localhost:9092",
        auto_offset_reset="earliest",
        enable_auto_commit=False,
        group_id=None,
        consumer_timeout_ms=15000,
        value_deserializer=lambda message: json.loads(message.decode("utf-8")),
    )

    country_counts = defaultdict(int)
    category_counts = defaultdict(int)
    session_counts = defaultdict(int)

    processed = 0

    for message in consumer:
        event = message.value

        cursor.execute(
            """
            INSERT INTO raw_events (
                event_id, event_time, event_type, session_id, country, main_category,
                clothing_model, colour, location, model_photography, price,
                price_band, page, year, month, day, event_order
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                int(event["event_id"]),
                event["event_time"],
                event["event_type"],
                int(event["session_id"]),
                int(event["country"]),
                int(event["main_category"]),
                event["clothing_model"],
                int(event["colour"]),
                int(event["location"]),
                int(event["model_photography"]),
                int(event["price"]),
                int(event["price_band"]),
                int(event["page"]),
                int(event["year"]),
                int(event["month"]),
                int(event["day"]),
                int(event["order"]),
            ),
        )

        country_counts[str(event["country"])] += 1
        category_counts[str(event["main_category"])] += 1
        session_counts[str(event["session_id"])] += 1
        processed += 1

        if processed % 5000 == 0:
            connection.commit()

    connection.commit()
    consumer.close()

    for country, count in country_counts.items():
        cursor.execute(
            "INSERT INTO stream_metrics (metric_name, dimension, metric_value) VALUES (?, ?, ?)",
            ("country_event_count", country, count),
        )

    for category, count in category_counts.items():
        cursor.execute(
            "INSERT INTO stream_metrics (metric_name, dimension, metric_value) VALUES (?, ?, ?)",
            ("category_event_count", category, count),
        )

    for session_id, count in session_counts.items():
        cursor.execute(
            "INSERT INTO stream_metrics (metric_name, dimension, metric_value) VALUES (?, ?, ?)",
            ("session_event_count", session_id, count),
        )

    connection.commit()
    connection.close()

    print(f"Kafka consumer processed {processed} events from topic: {topic_name}")
    print(f"Kafka streaming database saved to: {db_file}")


if __name__ == "__main__":
    main()
