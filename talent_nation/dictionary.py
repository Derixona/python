capitals = {"USA":"Washington D.C.", "India": "New Delhi", 
"China": "Beijing", "Russia": "Moscow"}
# print(f"Original Dictionary: {capitals}")

capitals.update({"Germany": "Berlin"})

#print(capitals.items())

for key, value in capitals.items():
    print(key, value)

#del capitals['USA']


