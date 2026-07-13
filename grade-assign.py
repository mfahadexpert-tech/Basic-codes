#Student ke marks (0-100) input lein. 90+ par "Grade A", 80-89 par "Grade B",
#  aur 70-79 "Grade C" or baki "F" print karein
marks=int(input("enetr your marks: "))
if marks>=90:
    print("A grade")
elif marks>=80:
    print("B grade")
elif marks>=70:
    print("C Grade")
else:
    print("F grade")