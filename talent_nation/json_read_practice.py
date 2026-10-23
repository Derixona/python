import json

with open("tickets.json", "r") as file:
    loaded_ticket = json.load(file)
    for x in loaded_ticket:
        print(f'{x["id"] } - {x["title"]}')
