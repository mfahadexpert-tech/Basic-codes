#Ek variable banayein time. Agar time 10 (baje) ke baad ka hai, 
# toh if-else ka use karke "Silent Mode
#On" print karein, warna "Ring Loud" print karein.
time=int(input("Enter current hour in 1-12"))
if time>10:
    print("silent mode is on")
else:
    print("ring loud")
