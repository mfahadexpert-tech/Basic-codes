class TaxCalculator:

    def calculate_tax(self, income, treaty_rate=None):

        if treaty_rate is None:
            return income * 0.10
        return income * treaty_rate

calc = TaxCalculator()
print(calc.calculate_tax(100000))
print(calc.calculate_tax(100000, 0.15))