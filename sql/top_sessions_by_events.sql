SELECT
    dimension AS session_id,
    metric_value AS total_events
FROM stream_metrics
WHERE metric_name = 'session_event_count'
ORDER BY metric_value DESC
LIMIT 10;
