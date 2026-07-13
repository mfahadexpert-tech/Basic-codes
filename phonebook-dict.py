#Contact Search: Aik phonebook dictionary banayein. .get() method ka istemal 
# karte hue kisi specific dost ka number search karein. Agar number na mile to "Contact Not Found" ka message dikhayen
phonebook = {
    "Ali": "03001234567",
    "Ahmed": "03111234567",
    "Sara": "03221234567"
}

name = input("Enter friend's name: ")

number = phonebook.get(name)

if number:
    print("Phone Number:", number)
else:
    print("Contact Not Found")