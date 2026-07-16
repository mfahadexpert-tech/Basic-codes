class Address:

    def __init__(self, city, pincode, state):
        self.__city = city
        self.__pincode = pincode
        self.__state = state

    def get_city(self):
        return self.__city

    def get_pincode(self):
        return self.__pincode

    def get_state(self):
        return self.__state

class Customer:
    def __init__(self, name, gender, address):
        self.name = name
        self.gender = gender
        self.address = address      # Aggregation

    def print_shipping_label(self):
        print(f"Shipping To: {self.name}")
        print(f"{self.address.get_city()}-{self.address.get_pincode()}, {self.address.get_state()}")

addr = Address("Lahore", 54000, "Punjab")
cust = Customer("Zain", "Male", addr)

cust.print_shipping_label()