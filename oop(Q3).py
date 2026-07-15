#Ek SmartBulb class banayein jismein ek attribute state = "OFF" ho.
# Isme ek method turn_on()
#banayein jo state ko "ON" kar de.
class SmartBulb:
    def __init__(self):
        self.state = "OFF"

    def turn_on(self):
        self.state = "ON"

bulb = SmartBulb()

print("Before:", bulb.state)
bulb.turn_on()
print("After:", bulb.state)