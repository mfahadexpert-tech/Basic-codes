#ATM Withdrawal Logic: Ek variable balance = 5000 rakhen. User se withdrawal_amount input lein.
#  Agar amount balance se zyada ho to "Insufficient Funds" print karein, warna remaining balance dikhayen .
#  Ride-Sharing Fare: Aik app ke liye logic likhen: Agar distance 5km se kam
#  hai to fare 100 PKR, agar 5-15km hai to 250 PKR, aur agar usse zyada hai to 500 PKR charge karein
distance = float(input("Enter distance in km: "))

if distance < 5:
    fare = 100
elif distance <= 15:
    fare = 250
else:
    fare = 500

print("Your Fare is:", fare, "PKR")