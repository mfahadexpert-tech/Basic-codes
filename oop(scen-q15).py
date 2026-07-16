class UserProfile:
    def __init__(self, name):
        self.name = name


user1 = UserProfile("Ali")

user2 = user1

user2.name = "akram"

print(user1.name)
print(user2.name)

print(id(user1))
print(id(user2))