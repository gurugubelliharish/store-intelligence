import json
from pathlib import Path

events_file = Path("backend/data/events/store2_events.jsonl")

entries = 0
exits = 0

with open(events_file, "r") as f:
    for line in f:

        event = json.loads(line)

        if event["event_type"] == "ENTRY":
            entries += 1

        elif event["event_type"] == "EXIT":
            exits += 1

print("\nStore Metrics\n")
print("Total Entries:", entries)
print("Total Exits:", exits)
print("Net Occupancy Change:", entries - exits)