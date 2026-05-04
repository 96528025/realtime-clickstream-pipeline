#!/bin/zsh

set -euo pipefail

PROJECT_DIR="/Users/angelren/Documents/projects/realtime-ecommerce-pipeline"
RUNTIME_DIR="$PROJECT_DIR/.kafka"
KAFKA_VERSION="4.2.0"
KAFKA_SCALA_VERSION="2.13"
KAFKA_HOME="$RUNTIME_DIR/kafka_${KAFKA_SCALA_VERSION}-${KAFKA_VERSION}"
TOPIC_NAME="clickstream-events"

"$KAFKA_HOME/bin/kafka-topics.sh" \
  --bootstrap-server localhost:9092 \
  --create \
  --if-not-exists \
  --topic "$TOPIC_NAME" \
  --partitions 3 \
  --replication-factor 1

echo "Kafka topic ready: $TOPIC_NAME"
