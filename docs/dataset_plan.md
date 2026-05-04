# Dataset Plan

## Selected Dataset
- Name: Clickstream Data for Online Shopping
- Source: UCI Machine Learning Repository
- Link: https://archive.ics.uci.edu/dataset/553/clickstream%2Bda

## Why This Dataset
- It contains sequential clickstream records suitable for replay-based streaming
- It includes session, country, product category, and page interaction fields
- It supports event-order processing and real-time aggregation use cases

## Main Fields
- year
- month
- day
- order
- country
- session ID
- page 1 (main category)
- page 2 (clothing model)
- colour
- location
- model photography
- price
- price 2
- page

## Planned Usage
- Store the raw dataset in `data/raw/`
- Standardize column names and sort events by session order
- Replay events in timestamp-like sequence using a Python producer
- Consume events and compute streaming metrics in SQLite

---

# 数据集方案

## 选定数据集
- 名称：Clickstream Data for Online Shopping
- 来源：UCI Machine Learning Repository
- 链接：https://archive.ics.uci.edu/dataset/553/clickstream%2Bda

## 为什么选择这个数据集
- 包含适合重放式流处理的顺序点击流记录
- 具备 session、国家、商品类目和页面交互字段
- 支持事件顺序处理和实时聚合场景

## 主要字段
- year：年份
- month：月份
- day：日期
- order：会话内点击顺序
- country：国家
- session ID：会话 ID
- page 1 (main category)：主商品类目
- page 2 (clothing model)：商品型号/商品编码
- colour：商品颜色
- location：页面展示位置
- model photography：模特展示类型
- price：价格区间
- price 2：价格区间二值化字段
- page：页面编号

## 计划用法
- 将原始数据存放到 `data/raw/`
- 标准化字段名并按会话顺序排序
- 使用 Python producer 按类时间顺序重放事件
- 使用 SQLite 计算并存储流式指标
