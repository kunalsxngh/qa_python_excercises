print("Welcome to Grade Calculator")
maths =  int(input("Please enter your maths grade: "))
chemistry =  int(input("Please enter your chemistry grade: "))
physics = int(input("Please enter your physics grade: "))

score = ((maths + chemistry + physics) / 300) * 100

print("Your percentage score is:", round(score, 2), "%")

if score >= 70:
    grade = "A"
elif score >= 60:
    grade = "B"
elif score >= 50:
    grade = "C"
elif score >= 40:
    grade = "D"
else:
    grade = "You failed"

print("You scored a grade of:", grade)