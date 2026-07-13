#Student ke marks (0-100) input lein. 90+ par "Grade A", 80-89 par "Grade B", aur baki par "Grade C" print karein
marks=int(input("enetr your marks: "))
if marks>=90:
    print("A grade")
elif marks>=80:
    print("B grade")
else:
    print("C grade")