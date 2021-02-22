def convert(number):
    solution = ""
    if number % 3 == 0:
        solution += "Pling"
    if number % 5 == 0:
       solution += "Plang"
    if number % 7 == 0:
        solution += "Plong"
    return f"{number}" if solution == "" else solution

