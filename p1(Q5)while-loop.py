#Ek while loop ka istemal karein jo 1 se 3 tak "Login Attempt X"
#  print kare taake 3 attempts ke baad
#system lock hone ka logic banaya ja sake.
attempt = 1

while attempt <= 3:
    print(f"Login Attempt {attempt}")
    attempt += 1

print("System Locked")