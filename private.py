class Employee:
    def __init__(self, name, salary):
        self.name = name          # Public
        self._department = "IT"   # Protected 
        self.__salary = salary    # Private

    def show(self):
        print(self.__salary)  # Private variable CAN be accessed inside class

e1 = Employee("Ali", 50000)

print(e1.name)        # Works: Ali
print(e1._department) #  Works but not recommended: IT
# print(e1.__salary)  #  Error: AttributeError

# But you CAN access it using name mangling:
print(e1.__salary) # Works: 50000. This is how Python "hides" it