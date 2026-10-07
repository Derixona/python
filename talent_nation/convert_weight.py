def solution(kilograms):
    weight = float(kilograms)
    kilo = weight
    gram = weight * 1000
    pounds = round(weight * 2.20462,2)
    return f"Kilograms: {kilo}\nGrams: {gram}\nPounds: {pounds}"
print(solution(1))