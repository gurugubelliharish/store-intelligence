import json
from pathlib import Path

input_file = Path("backend/data/events/store2_events.jsonl")
output_file = Path("backend/data/events/store2_events_cleaned.jsonl")

occupancy = 0
cleaned_events = []

with open(input_file, "r") as f:
    for line in f:

        event = json.loads(line)

        if event["event_type"] == "ENTRY":
            occupancy += 1
            cleaned_events.append(event)

        elif event["event_type"] == "EXIT":

            if occupancy > 0:
                occupancy -= 1
                cleaned_events.append(event)

            else:
                print(
                    "Removed invalid EXIT:",
                    event["visitor_id"]
                )

with open(output_file, "w") as f:
    for event in cleaned_events:
        f.write(json.dumps(event) + "\n")

print("\nCleaning Complete")
print("Valid Events:", len(cleaned_events))
print("Final Occupancy:", occupancy)
print("Saved:", output_file)