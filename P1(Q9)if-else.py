#Ek if-elif-else block banayein jo user input ("Red", "Yellow", "Green") ke mutabiq instructions print
#kare: Red par "Stop", Yellow par "Slow Down", Green par "Go".
color = input("Enter traffic light color: ")

if color == "Red":
    print("Stop")
elif color == "Yellow":
    print("Slow Down")
elif color == "Green":
    print("Go")
else:
    print("Invalid Color")