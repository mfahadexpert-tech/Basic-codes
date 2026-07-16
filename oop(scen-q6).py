class Portfolio:
    def __init__(self, cash, stock_value):
        self.cash = cash
        self.stock_value = stock_value

    def __add__(self, other):
        return Portfolio(
            self.cash + other.cash,
            self.stock_value + other.stock_value
        )

    def display(self):
        print("Cash:", self.cash)
        print("Stock Value:", self.stock_value)


p1 = Portfolio(5000, 12000)
p2 = Portfolio(3000, 4000)
p3 = p1 + p2
p3.display()