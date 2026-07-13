#Login System Mockup: Ek dictionary mein username aur password store karein. 
# User se input lein aur if statement ke zariye check karein ke input kiya gaya data dictionary ke data se match karta hai ya nahi
login = {
    "username": "admin",
    "password": "12345"
}

username = input("Enter Username: ")
password = input("Enter Password: ")

if username == login["username"] and password == login["password"]:
    print("Login Successful")
else:
    print("Invalid Username or Password")