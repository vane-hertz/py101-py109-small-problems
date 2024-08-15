def get_grade(num1, num2, num3):
    average = (num1 + num2 + num3) / 3
    if average <= 100 and average >= 90:
        return "A"
    elif average < 90 and average >= 80:
        return "B"
    elif average < 80 and average >= 70:
        return "C"
    elif average < 70 and average >= 60:
        return "D"
    elif average < 60 and average >= 0:
        return "F"