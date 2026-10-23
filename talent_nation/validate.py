def validate_ticket(ticket)  -> bool:
 
 if "id" in ticket and "title" in ticket and "status" in ticket:
            if isinstance(ticket["id"], str) and isinstance(ticket["title"],str) and isinstance(ticket["status"], str):
              if ticket["id"].strip() != "" and ticket["title"].strip()!="" and ticket["status"].strip()!="":
                 allowed_status = ["open", "in_progress", "resolved"]
                 if ticket["status"] in allowed_status:
                    return True
 return False
    
if __name__ == "__main__":

 ticket_a = {
    "id":"T001",
    "title": "Network failure",
    "status": "open"
}

ticket_b = {
    "id": "",
    "title": "Network failure",
    "status": "open"
}

ticket_c = {
    "id": "T003",
    "title": "Projector failure",
    "status": "banana"
}

print(validate_ticket(ticket_a))
print(validate_ticket(ticket_b))
print(validate_ticket(ticket_c))