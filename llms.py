# def patrol_bounds(positions):
#     row = []
#     col = []
#     for ro, co in positions:
#         row.append(ro)
#         col.append(co)
#     return (min(row), max(row), min(col), max(col))
   

# if __name__ == "__main__":
#     pos = [[1,3],[4,1],[2,5]]
#     print(type(pos))
#     print(patrol_bounds(pos))


# def normalise_code(raw):
#     normal_text = raw.lower().replace(" ", "")
#     #print(help(str))
#     return normal_text

# print(normalise_code(" AL PHA "))


# def censor(message, word):
#     if word == "":
#         return message
#     replace_message = message.replace(word, "[REDACTED]")
#     return replace_message
# print(censor("all clear","enemy"))



def is_valid_transmission(message):
    start = message.startswith("BEGIN")
    end = message.endswith("END")
    strick = "//" in message
    if message and start and strick and end:
        return True
    return False
print(is_valid_transmission("move out//END"))





