name = input("Hi, what is your name?: ")
homework = int(input("What was your homework score?:"))
assessment = int(input("What was your assessment score?:"))
finalExam = int(input("What was your final exam score?:"))

def gradeCalcuator(homework, assessment, finalExam, name):
    finalScore = (homework/25) + (assessment/50) + (finalExam/100)
    finalScore = round(((finalScore * 100) / 3), 2)
    if finalScore >= 70:
        grade = "A"
    elif finalScore >= 60:
        grade = "B"
    elif finalScore >= 50:
        grade = "C"
    elif finalScore >= 40:
        grade = "D"
    else:
        grade = "You failed"

    return "Thanks {}, you scored {}% and your grade was {}".format(name, finalScore, grade)


print(gradeCalcuator(homework, assessment, finalExam, name))