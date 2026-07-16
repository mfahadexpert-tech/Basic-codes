class Vehicle:

    def __init__(self, price, brand, engine_no):
        self.price = price
        self.brand = brand
        self.engine_no = engine_no


class ElectricCar(Vehicle):

    def __init__(self, price, brand, engine_no, battery_capacity, charging_time):
        super().__init__(price, brand, engine_no)
        self.battery_capacity = battery_capacity
        self.charging_time = charging_time

    def display(self):
        print(self.brand)
        print(self.price)
        print(self.engine_no)
        print(self.battery_capacity)
        print(self.charging_time)


car = ElectricCar(25000, "Tesla", "EV909", "100kWh", "4 Hours")
car.display()