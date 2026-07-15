#Ek HotelRoom class banayein jismein is_occupied = True ho. Ek method checkout() banayein
#jo is value ko update karke False kar de.
class HotelRoom:
    def __init__(self):
        self.is_occupied = True
    def update(self):
        self.is_occupied = False
s=HotelRoom()
print(s.is_occupied)
s.update()
print(s.is_occupied)

