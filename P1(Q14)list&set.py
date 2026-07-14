#Ek system mein duplicate email IDs list mein aagayi hain.
# Us list ko pehle set mein convert karein taake
#duplicates uṛ jayen, phir .add() use kar ke ek naya email add karein aur print karein
emails = [
    "ali@gmail.com",
    "ahmad@gmail.com",
    "ali@gmail.com"
]

unique_emails = set(emails)

unique_emails.add("hamza@gmail.com")

print(unique_emails)