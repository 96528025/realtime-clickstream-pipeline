SELECT
    dimension AS country,
    metric_value AS total_events
FROM stream_metrics
WHERE metric_name = 'country_event_count'
ORDER BY metric_value DESC
LIMIT 10;
