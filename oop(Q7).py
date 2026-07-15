#Ek DatabaseConfig class banayein jismein host aur port ko aik tuple attribute credentials =
#("localhost", 3306) mein store kiya jaye taake credentials immutable rahin.
class DatabaseConfig:
    credentials = ("localhost", 3306)

db = DatabaseConfig()

print("Host:", db.credentials[0])
print("Port:", db.credentials[1])