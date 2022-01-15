
def calculate_grade(grade):
    letter = "F"
    if grade > 80:
        letter = "A"
    elif grade > 70:
        letter = "B"
    elif grade > 60:
        letter = "C"
    elif grade > 50:
        letter = "D"
    return letter


print(calculate_grade(81))