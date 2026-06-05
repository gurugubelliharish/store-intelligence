import subprocess
import sys

steps = [

    # -----------------------------------
    # Entry / Exit Analytics
    # -----------------------------------

    "backend/detection/generate_events.py",
    "backend/analytics/clean_events.py",
    "backend/analytics/generate_sessions.py",
    "backend/analytics/occupancy_tracker_cleaned.py",
    "backend/analytics/store_dashboard.py",

    # -----------------------------------
    # Zone Analytics
    # -----------------------------------

    "backend/detection/zone_journey.py",
    "backend/detection/dwell_time.py",

    # -----------------------------------
    # Final Metrics Export
    # -----------------------------------

    "backend/analytics/export_metrics.py"
]

for step in steps:

    print("\n" + "=" * 60)
    print(f"Running: {step}")
    print("=" * 60)

    subprocess.run(
        [sys.executable, step],
        check=True
    )

print("\n" + "=" * 60)
print("STORE INTELLIGENCE PIPELINE COMPLETED")
print("=" * 60)