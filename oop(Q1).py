#Ek online store ke liye Product class banayein jismein n
#ame aur price ke default attributes hon. Is
#class ke do objects (e.g., Laptop aur Smartphone)
# instantiate karein aur dono ki details print karein.
class Product:
    name = "Unknown"
    price = 0

# Objects
laptop = Product()
laptop.name = "Laptop"
laptop.price = 80000

smartphone = Product()
smartphone.name = "Smartphone"
smartphone.price = 50000

print("Product 1:", laptop.name, "-", laptop.price)
print("Product 2:", smartphone.name, "-", smartphone.price)