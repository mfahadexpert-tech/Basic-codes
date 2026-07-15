#Ek system user profile ke liye User class banayein.
#  Har user ka apna username aur status =
#"Active" hona chahiye. Ek naya user object banayein 
# aur uska status print karein.
class User:
    def __init__(self, username):
        self.username = username
        self.status = "Active"

user1 = User("Fahad")

print("Username:", user1.username)
print("Status:", user1.status)