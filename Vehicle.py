# =====================================
# Parent Class
# =====================================

class Vehicle:

    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def calculate_tax(self):
        print("Tax Calculation Not Defined")


# =====================================
# Child Class
# =====================================

class GasCar(Vehicle):

    def __init__(self, brand, model, price):
        super().__init__(brand, model, price)

    def calculate_tax(self):
        tax = self.price * 0.15
        return tax


# =====================================
# Child Class
# =====================================

class ElectricCar(Vehicle):

    def __init__(self, brand, model, price):
        super().__init__(brand, model, price)

    def calculate_tax(self):
        return 0


# =====================================
# Testing
# =====================================

car1 = GasCar("Toyota", "Corolla", 4500000)
car2 = ElectricCar("Tesla", "Model 3", 12000000)
car3 = GasCar("Honda", "Civic", 5000000)
car4 = ElectricCar("BYD", "Atto 3", 9000000)

fleet = [car1, car2, car3, car4]

print("\n========== Fleet Tax Report ==========\n")

for car in fleet:

    print("Brand :", car.brand)
    print("Model :", car.model)
    print("Price :", car.price)
    print("Tax   :", car.calculate_tax())
    print("-------------------------------------")