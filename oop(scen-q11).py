class CartItem:
    def __init__(self, item_name, quantity, price):
        self.item_name = item_name
        self.quantity = quantity
        self.price = price

cart = [
    CartItem("Mouse", 2, 800),
    CartItem("Keyboard", 1, 2000),
    CartItem("USB", 3, 500)
]

total = 0

for item in cart:
    total += item.quantity * item.price

print("Total =", total)