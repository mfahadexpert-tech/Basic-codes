#User se product ki price input lein, usay int mein 
# typecast karein, aur 10% discount minus kar ke final
#price print karein.
price = int(input("Enter product price: "))
discount = price * 0.10
final_price = price - discount
print("Final Price =", final_price)