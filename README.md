# Real-Time E-commerce Clickstream Pipeline

This project is a real-time e-commerce data engineering project built on the UCI Clickstream Data for Online Shopping dataset.

## Current Scope
- Phase 1 completed: local streaming simulation with a Python producer-consumer pipeline
- Phase 2 completed: Kafka-based event streaming with a real broker, topic, producer, and consumer

## Goals
- Replay historical clickstream events as a simulated real-time stream
- Build a producer-consumer pipeline for sequential event processing
- Generate streaming metrics such as page views, top categories, and country-level activity
- Store processed events and aggregated metrics for downstream analysis

## Dataset
- Source: UCI Clickstream Data for Online Shopping
- Domain: E-commerce clickstream events

## Key Results
- Standardized 165,474 raw clickstream records into an event table with 17 streaming-ready fields
- Replayed the full event history through both a local producer-consumer pipeline and a Kafka-based event pipeline
- Produced and consumed all 165,474 events through the `clickstream-events` Kafka topic and stored results in SQLite
- Generated stream metrics for country-level activity, category activity, and session-level event volume
- Identified country `29` as the dominant traffic source, main category `1` as the most active category, and session `22433` as the most active session

## Kafka Architecture
- Historical clickstream dataset as the event source
- Python Kafka producer to replay events in sequence
- Kafka topic for event transport and decoupling
- Python Kafka consumer to process incoming events
- SQLite sink for processed events and real-time aggregates

## Project Structure
- `data/`: raw and processed datasets
- `notebooks/`: exploration and validation
- `scripts/`: ingestion, replay, and streaming scripts
- `sql/`: SQL queries for downstream analytics
- `docs/`: project notes and documentation

## SQL Analytics
- Top countries by streamed event volume
- Top categories by streamed event volume
- Top sessions by event count
- SQLite used as the Kafka-backed streaming sink and analytics database

---

# 实时电商点击流管道项目

这是一个基于 UCI Clickstream Data for Online Shopping 数据集构建的实时电商数据工程项目。

## 当前阶段
- 第一阶段已完成：基于 Python producer-consumer 的本地流式模拟
- 第二阶段已完成：接入真实 Kafka broker、topic、producer 和 consumer

## 项目目标
- 将历史点击流事件重放为模拟实时数据流
- 搭建生产者-消费者式顺序事件处理管道
- 生成页面浏览量、热门类目、国家维度活跃度等流式指标
- 存储处理后的事件和聚合指标，供下游分析使用

## 数据集
- 来源：UCI Clickstream Data for Online Shopping
- 领域：电商点击流事件

## 核心结果
- 将 165,474 条原始点击流记录标准化为包含 17 个字段的流处理事件表
- 通过本地 producer-consumer 管道和 Kafka 事件流管道重放全部历史事件，并将结果写入 SQLite
- 通过 `clickstream-events` Kafka topic 完整生产和消费 165,474 条事件
- 生成国家维度、类目维度和 session 维度的流式聚合指标
- 识别出国家 `29` 为主要流量来源、主类目 `1` 为最活跃类目、session `22433` 为最活跃会话

## Kafka 架构
- 历史点击流数据集作为事件源
- 使用 Python Kafka producer 按顺序重放事件
- 使用 Kafka topic 作为事件传输层
- 使用 Python Kafka consumer 处理输入事件
- 使用 SQLite 存储处理后的事件和实时聚合指标

## 项目结构
- `data/`：原始数据和处理后数据
- `notebooks/`：探索分析与验证
- `scripts/`：数据摄取、重放与流处理脚本
- `sql/`：下游分析 SQL
- `docs/`：项目说明和过程文档

## SQL 分析层
- 国家维度事件量分析
- 类目维度事件量分析
- session 维度事件数分析
- 使用 SQLite 作为 Kafka 流处理落库和分析数据库
