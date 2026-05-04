#!/bin/zsh

set -euo pipefail

PID_FILE="/Users/angelren/Documents/projects/realtime-ecommerce-pipeline/.kafka/kafka.pid"

if [ ! -f "$PID_FILE" ]; then
  echo "Kafka PID file not found."
  exit 0
fi

PID="$(cat "$PID_FILE")"

if kill -0 "$PID" 2>/dev/null; then
  kill "$PID"
  echo "Stopped Kafka process $PID"
else
  echo "Kafka process $PID is not running"
fi

rm -f "$PID_FILE"
