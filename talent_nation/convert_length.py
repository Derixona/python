def solution(meters):
    
    convert = float(meters)
    cent = convert * 100
    mil = convert * 1000
    return f"Centimeters: {cent}\nMillimeters: {mil}"
if __name__ == "__main__":
    print(solution("3"))