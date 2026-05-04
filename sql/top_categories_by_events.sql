SELECT
    dimension AS main_category,
    metric_value AS total_events
FROM stream_metrics
WHERE metric_name = 'category_event_count'
ORDER BY metric_value DESC
LIMIT 10;
