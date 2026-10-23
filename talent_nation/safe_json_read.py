import json

try:
    with open("tickets.json", "r") as file:
        loaded_tickets = json.load(file)
    print(f'Successfully loaded {len(loaded_tickets)} tickets.')

except FileNotFoundError:
    print('Error: tickets.json was not found.')


except json.JSONDecodeError:
    print('Error: tickets.json contains invalid JSON')
