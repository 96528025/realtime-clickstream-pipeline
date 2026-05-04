# Roadmap

## Phase 1 Completed
- Downloaded the official UCI clickstream dataset
- Standardized the raw semicolon-delimited CSV into an event table
- Replayed historical events through a local producer-consumer pipeline
- Stored processed events and aggregate metrics in SQLite
- Added SQL queries for country, category, and session-level event analysis

## Phase 2 Planned
- Add a Kafka broker runtime
- Replace the in-memory queue with Kafka topics
- Implement a Kafka producer for event replay
- Implement a Kafka consumer for downstream aggregation
- Expand stream metrics to include time-windowed analytics

---

# 路线图

## 第一阶段已完成
- 下载 UCI 官方点击流数据集
- 将分号分隔的原始 CSV 标准化为事件表
- 通过本地 producer-consumer 管道重放历史事件
- 将处理后的事件和聚合指标写入 SQLite
- 增加国家、类目和 session 维度的 SQL 分析

## 第二阶段计划
- 增加 Kafka broker 运行环境
- 使用 Kafka topic 替换内存队列
- 实现用于事件重放的 Kafka producer
- 实现下游聚合的 Kafka consumer
- 扩展为带时间窗口的流式指标分析
