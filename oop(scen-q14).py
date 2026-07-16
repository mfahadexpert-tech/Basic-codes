class Validator:
    def validate(self):
        print("Parent Validation")


class StrictValidator(Validator):
    def validate(self):
        super().validate()
        print("Strict Validation")

obj = StrictValidator()
obj.validate()