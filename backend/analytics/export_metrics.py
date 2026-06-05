import json

# --------------------------------------------------
# Read cleaned events
# --------------------------------------------------

with open(
    "backend/data/events/store2_events_cleaned.jsonl",
    "r"
) as f:
    events = [json.loads(line) for line in f]

# --------------------------------------------------
# Entry / Exit counts
# --------------------------------------------------

entries = sum(
    1 for e in events
    if e["event_type"] == "ENTRY"
)

exits = sum(
    1 for e in events
    if e["event_type"] == "EXIT"
)

# --------------------------------------------------
# Occupancy calculation
# --------------------------------------------------

occupancy = 0
peak_occupancy = 0

for event in events:

    if event["event_type"] == "ENTRY":
        occupancy += 1

    elif event["event_type"] == "EXIT":
        occupancy -= 1

    peak_occupancy = max(
        peak_occupancy,
        occupancy
    )

final_occupancy = occupancy

# --------------------------------------------------
# Read dwell analytics
# --------------------------------------------------

with open(
    "backend/data/analytics/dwell_summary.json",
    "r"
) as f:
    avg_dwell_time = json.load(f)

# --------------------------------------------------
# Read zone journey analytics
# --------------------------------------------------

with open(
    "backend/data/analytics/zone_summary.json",
    "r"
) as f:
    zone_transitions = json.load(f)

# --------------------------------------------------
# Build metrics
# --------------------------------------------------

metrics = {
    "store_id": "STORE_BLR_002",
    "total_entries": entries,
    "total_exits": exits,
    "peak_occupancy": peak_occupancy,
    "final_occupancy": final_occupancy,
    "avg_dwell_time": avg_dwell_time,
    "zone_transitions": zone_transitions
}

# --------------------------------------------------
# Save metrics
# --------------------------------------------------

with open(
    "backend/data/store_metrics.json",
    "w"
) as f:
    json.dump(
        metrics,
        f,
        indent=4
    )

print("\nMetrics exported successfully")
print(json.dumps(metrics, indent=4))