class SmartLock:
    def __init__(self):
        self.__pin = "0000"

    def set_pin(self, new_pin):

        if len(new_pin) == 4 and new_pin.isdigit():
            self.__pin = new_pin
            print("PIN Updated Successfully.")
        else:
            print("Invalid PIN.")

    def unlock(self, input_pin):

        if input_pin == self.__pin:
            print("Unlocked")
        else:
            print("Wrong PIN")


lock = SmartLock()

lock.set_pin("9081")

lock.unlock("9081")