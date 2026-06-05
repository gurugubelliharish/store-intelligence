import json
from pathlib import Path

events_file = Path(
    "backend/data/events/store2_events_cleaned.jsonl"
)

entries = 0
exits = 0
occupancy = 0
peak_occupancy = 0

with open(events_file, "r") as f:

    for line in f:

        event = json.loads(line)

        if event["event_type"] == "ENTRY":
            entries += 1
            occupancy += 1

        elif event["event_type"] == "EXIT":
            exits += 1
            occupancy -= 1

        peak_occupancy = max(
            peak_occupancy,
            occupancy
        )

print("\n===== STORE DASHBOARD =====\n")

print("Total Entries      :", entries)
print("Total Exits        :", exits)
print("Peak Occupancy     :", peak_occupancy)
print("Final Occupancy    :", occupancy)

if entries > 0:
    completion_rate = (exits / entries) * 100
    print(
        "Visit Completion %:",
        round(completion_rate, 2)
    )
else:
    print("Visit Completion %: 0")