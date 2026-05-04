#!/bin/zsh

set -euo pipefail

PROJECT_DIR="/Users/angelren/Documents/projects/realtime-ecommerce-pipeline"
RUNTIME_DIR="$PROJECT_DIR/.kafka"
KAFKA_VERSION="4.2.0"
KAFKA_SCALA_VERSION="2.13"
KAFKA_ARCHIVE="kafka_${KAFKA_SCALA_VERSION}-${KAFKA_VERSION}.tgz"
KAFKA_URL="https://downloads.apache.org/kafka/${KAFKA_VERSION}/${KAFKA_ARCHIVE}"
KAFKA_HOME="$RUNTIME_DIR/kafka_${KAFKA_SCALA_VERSION}-${KAFKA_VERSION}"
KAFKA_CONFIG="$RUNTIME_DIR/server.properties"
KAFKA_LOG_DIR="$RUNTIME_DIR/kraft-combined-logs"
KAFKA_PID_FILE="$RUNTIME_DIR/kafka.pid"
KAFKA_SERVER_LOG="$RUNTIME_DIR/kafka-server.log"
KAFKA_CLUSTER_ID_FILE="$RUNTIME_DIR/cluster.id"
BROKER_PORT="19092"
CONTROLLER_PORT="19093"

mkdir -p "$RUNTIME_DIR"

if [ ! -d "$KAFKA_HOME" ]; then
  curl -L "$KAFKA_URL" -o "$RUNTIME_DIR/$KAFKA_ARCHIVE"
  tar -xzf "$RUNTIME_DIR/$KAFKA_ARCHIVE" -C "$RUNTIME_DIR"
fi

cp "$KAFKA_HOME/config/server.properties" "$KAFKA_CONFIG"
{
  echo ""
  echo "log.dirs=$KAFKA_LOG_DIR"
  echo "listeners=PLAINTEXT://:${BROKER_PORT},CONTROLLER://:${CONTROLLER_PORT}"
  echo "advertised.listeners=PLAINTEXT://localhost:${BROKER_PORT}"
} >> "$KAFKA_CONFIG"

if [ ! -f "$KAFKA_CLUSTER_ID_FILE" ]; then
  "$KAFKA_HOME/bin/kafka-storage.sh" random-uuid > "$KAFKA_CLUSTER_ID_FILE"
fi

if [ ! -d "$KAFKA_LOG_DIR" ] || [ -z "$(ls -A "$KAFKA_LOG_DIR" 2>/dev/null)" ]; then
  mkdir -p "$KAFKA_LOG_DIR"
  "$KAFKA_HOME/bin/kafka-storage.sh" format --standalone -t "$(cat "$KAFKA_CLUSTER_ID_FILE")" -c "$KAFKA_CONFIG"
fi

if [ -f "$KAFKA_PID_FILE" ] && kill -0 "$(cat "$KAFKA_PID_FILE")" 2>/dev/null; then
  echo "Kafka is already running with PID $(cat "$KAFKA_PID_FILE")"
  exit 0
fi

nohup "$KAFKA_HOME/bin/kafka-server-start.sh" "$KAFKA_CONFIG" > "$KAFKA_SERVER_LOG" 2>&1 &
echo $! > "$KAFKA_PID_FILE"

sleep 8

if kill -0 "$(cat "$KAFKA_PID_FILE")" 2>/dev/null; then
  echo "Kafka started successfully with PID $(cat "$KAFKA_PID_FILE")"
  echo "Kafka log: $KAFKA_SERVER_LOG"
else
  echo "Kafka failed to start. Check log: $KAFKA_SERVER_LOG"
  exit 1
fi
