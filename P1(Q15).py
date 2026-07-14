#Ek dictionary banayein (name, roll_no, marks). Result hide karne
# ke liye .pop() method use kar ke
#dictionary se marks remove karein aur updated data dikhayein.

student = {
    "name": "Ali",
    "roll_no": 101,
    "marks": 88
}

removed_marks = student.pop("marks")

print("Removed Marks:", removed_marks)
print(student)