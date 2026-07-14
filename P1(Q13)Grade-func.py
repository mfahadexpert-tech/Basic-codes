#Ek function calculate_grade(marks) banayein jo marks 
# check kar ke return kare: >90 pe "A",
#>80 pe "B", aur baki pe "C".

def calculate_grade(marks):
    if marks > 90:
        return "A"
    elif marks > 80:
        return "B"
    else:
        return "C"

marks = int(input("Enter Marks: "))
grade = calculate_grade(marks)

print("Grade:", grade)