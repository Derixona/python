def solution(celsius):
    change = float(celsius)
    fahrenheit = (change * 1.8) + 32
    round = float(fahrenheit)
    return round

print(solution("25"))