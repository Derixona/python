def solution(value):
    try:
        number = float(value)
        result = number * 2
    except ValueError:
        return "Invalid Input"
    return result
print(solution("hello"))
