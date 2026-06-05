import json
from pathlib import Path

events_file = Path("backend/data/events/store2_events.jsonl")

events = []

with open(events_file, "r") as f:
    for line in f:
        events.append(json.loads(line))

events.sort(key=lambda x: x["timestamp"])

visitor_sessions = {}

for event in events:

    visitor_id = event["visitor_id"]

    if visitor_id not in visitor_sessions:
        visitor_sessions[visitor_id] = {
            "entries": 0,
            "exits": 0
        }

    if event["event_type"] == "ENTRY":
        visitor_sessions[visitor_id]["entries"] += 1

    elif event["event_type"] == "EXIT":
        visitor_sessions[visitor_id]["exits"] += 1

print("\nVisitor Summary\n")

for visitor_id, stats in visitor_sessions.items():

    entries = stats["entries"]
    exits = stats["exits"]

    if entries == exits:
        status = "COMPLETE"

    elif entries > exits:
        status = "INSIDE_STORE"

    else:
        status = "DATA_ISSUE"

    print(
        visitor_id,
        "| Entries =", entries,
        "| Exits =", exits,
        "| Status =", status
    )