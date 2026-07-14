def calculate_bill(price, tax=5):
    total = price + (price * tax / 100)
    return total

print(calculate_bill(1000))
print(calculate_bill(1000, 10))