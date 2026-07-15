#Ek Profile class banayein. Ek method restrict_access() likhein jo user ka status "Banned" set
#kar de taake system use block kar sake.
class Profile:
    def __init__(self):
        self.status = "Active"

    def restrict_access(self):
        self.status = "Banned"

user = Profile()

print("Before:", user.status)
user.restrict_access()
print("After:", user.status)