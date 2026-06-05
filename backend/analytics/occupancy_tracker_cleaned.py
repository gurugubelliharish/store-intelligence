import json
from pathlib import Path

events_file = Path(
    "backend/data/events/store2_events_cleaned.jsonl"
)

current_occupancy = 0
max_occupancy = 0

events = []

with open(events_file, "r") as f:
    for line in f:
        events.append(json.loads(line))

events.sort(key=lambda x: x["timestamp"])

print("\nCleaned Occupancy Timeline\n")

for event in events:

    if event["event_type"] == "ENTRY":
        current_occupancy += 1

    elif event["event_type"] == "EXIT":
        current_occupancy -= 1

    max_occupancy = max(max_occupancy, current_occupancy)

    print(
        event["timestamp"],
        "|",
        event["event_type"],
        "| Occupancy =",
        current_occupancy
    )

print("\nPeak Occupancy:", max_occupancy)
print("Final Occupancy:", current_occupancy)