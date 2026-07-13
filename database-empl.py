#Employee Database: Ek dictionary banayein jis mein 
# name, designation, aur salary ho. Phir user se pooch kar
#  uski salary update karein aur ek naya key department add karein
employee = {
    "name": "Ali",
    "designation": "Software Engineer",
    "salary": 50000
}

new_salary = int(input("Enter new salary: "))
employee["salary"] = new_salary

department = input("Enter department: ")
employee["department"] = department

print(employee)