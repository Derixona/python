import json

tickets = [
    {"id": "T001", "title": "Projector failure"},
    {"id": "T002", "title": "Network outage"},
    {"id": "T003", "title": "Keyboard not working"}
]
with open("tickets.json", "w") as file:
    json.dump(tickets, file, indent=4)

print("json written to file [ticket.json] successfully.")