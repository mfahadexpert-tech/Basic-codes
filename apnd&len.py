#Lists & Slicing Product Inventory: Ek list banaein jis mein 5 products ke naam hon. User
#  se unka "6th product" input lein aur use .append() ke zariye add karein, phir list ki 
# total length print karein
products = ["Laptop", "Mouse", "Keyboard", "Monitor", "Printer"]

new_product = input("Enter the 6th product: ")

products.append(new_product)

print("Updated Product List:", products)
print("Total Products:", len(products))