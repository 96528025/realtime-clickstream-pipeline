# Roadmap

## Phase 1 Completed
- Downloaded the official UCI clickstream dataset
- Standardized the raw semicolon-delimited CSV into an event table
- Replayed historical events through a local producer-consumer pipeline
- Stored processed events and aggregate metrics in SQLite
- Added SQL queries for country, category, and session-level event analysis

## Phase 2 Completed
- Connected the project to a real Kafka broker
- Replaced the in-memory queue path with a Kafka topic
- Implemented a Kafka producer for event replay
- Implemented a Kafka consumer for downstream aggregation
- Persisted Kafka-consumed results into a separate SQLite sink

## Next Improvements
- Add time-windowed streaming metrics
- Add more advanced clickstream session analytics
- Containerize the broker and pipeline for easier portability

---

# 路线图

## 第一阶段已完成
- 下载 UCI 官方点击流数据集
- 将分号分隔的原始 CSV 标准化为事件表
- 通过本地 producer-consumer 管道重放历史事件
- 将处理后的事件和聚合指标写入 SQLite
- 增加国家、类目和 session 维度的 SQL 分析

## 第二阶段已完成
- 将项目接入真实 Kafka broker
- 使用 Kafka topic 替换内存队列路径
- 实现用于事件重放的 Kafka producer
- 实现下游聚合的 Kafka consumer
- 将 Kafka 消费结果写入独立的 SQLite 落库

## 后续优化
- 增加带时间窗口的流式指标
- 增加更深入的 clickstream session 分析
- 将 broker 和管道容器化，提升可移植性
