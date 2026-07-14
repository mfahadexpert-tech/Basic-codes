#1 se 10 tak user IDs ko for loop se traverse karein. Jab ID 5 aaye
#  (jo banned user hai), toh continue
#statement ka istemal kar ke usay skip kar dein aur baki IDs par notification bhejein.
for user_id in range(1, 11):
    if user_id == 5:
        continue

    print(f"Notification sent to User {user_id}")