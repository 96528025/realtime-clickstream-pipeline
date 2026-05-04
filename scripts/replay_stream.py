import queue
import sqlite3
import threading
import time
from collections import defaultdict

import pandas as pd


input_file = "/Users/angelren/Documents/projects/realtime-ecommerce-pipeline/data/processed/clickstream_events.csv"
db_file = "/Users/angelren/Documents/projects/realtime-ecommerce-pipeline/data/processed/realtime_clickstream.db"

EVENT_BATCH_SIZE = 5000
REPLAY_DELAY_SECONDS = 0.0001


def create_tables(connection):
    cursor = connection.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS raw_events (
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
        CREATE TABLE IF NOT EXISTS stream_metrics (
            metric_name TEXT,
            dimension TEXT,
            metric_value INTEGER
        )
        """
    )
    connection.commit()


def producer(df, event_queue):
    for row in df.itertuples(index=False):
        event_queue.put(row)
        time.sleep(REPLAY_DELAY_SECONDS)
    event_queue.put(None)


def consumer(event_queue, connection):
    cursor = connection.cursor()

    country_counts = defaultdict(int)
    category_counts = defaultdict(int)
    session_counts = defaultdict(int)

    processed = 0

    while True:
        event = event_queue.get()
        if event is None:
            break

        cursor.execute(
            """
            INSERT INTO raw_events (
                event_id, event_time, event_type, session_id, country, main_category,
                clothing_model, colour, location, model_photography, price,
                price_band, page, year, month, day, event_order
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                int(event.event_id),
                str(event.event_time),
                event.event_type,
                int(event.session_id),
                int(event.country),
                int(event.main_category),
                event.clothing_model,
                int(event.colour),
                int(event.location),
                int(event.model_photography),
                int(event.price),
                int(event.price_band),
                int(event.page),
                int(event.year),
                int(event.month),
                int(event.day),
                int(event.order),
            ),
        )

        country_counts[str(event.country)] += 1
        category_counts[str(event.main_category)] += 1
        session_counts[str(event.session_id)] += 1
        processed += 1

        if processed % EVENT_BATCH_SIZE == 0:
            connection.commit()

    connection.commit()

    cursor.execute("DELETE FROM stream_metrics")

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
    print(f"Stream replay completed. Processed events: {processed}")


def main():
    df = pd.read_csv(input_file, parse_dates=["event_time"])

    connection = sqlite3.connect(db_file, check_same_thread=False)
    create_tables(connection)

    event_queue = queue.Queue(maxsize=1000)

    producer_thread = threading.Thread(target=producer, args=(df, event_queue))
    consumer_thread = threading.Thread(target=consumer, args=(event_queue, connection))

    producer_thread.start()
    consumer_thread.start()

    producer_thread.join()
    consumer_thread.join()

    connection.close()
    print(f"Streaming database saved to: {db_file}")


if __name__ == "__main__":
    main()
