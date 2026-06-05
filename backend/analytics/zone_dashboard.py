journeys = {
    "CENTER -> LEFT": 3,
    "CENTER -> RIGHT": 6,
    "LEFT -> CENTER": 5,
    "RIGHT -> CENTER": 4
}

print("\n===== ZONE ANALYTICS DASHBOARD =====\n")

total_transitions = sum(journeys.values())

for path, count in sorted(
    journeys.items(),
    key=lambda x: x[1],
    reverse=True
):
    percentage = (count / total_transitions) * 100

    print(
        f"{path:<20} "
        f"{count:>3} transitions "
        f"({percentage:.1f}%)"
    )

print("\nTotal Zone Transitions:", total_transitions)