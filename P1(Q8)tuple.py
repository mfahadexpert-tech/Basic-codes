#Database ka Host aur Port ek tuple mein store karein aur 
# code mein usay change karne ki koshish
#karein taake error aaye aur sabit ho ke credentials (tuples) safe hain.
credentials = ("localhost", 3306)
print(credentials)
credentials[0] = "127.0.0.1"