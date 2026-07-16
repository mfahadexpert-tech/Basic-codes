class PaymentGateway:

    def process_payment(self, amount):
        print("Processing Payment:", amount)


class JazzCash(PaymentGateway):

    def process_payment(self, amount):
        fee = amount * 0.02
        print(f"JazzCash Payment: {amount} Fee: {fee}")


class EasyPaisa(PaymentGateway):

    def process_payment(self, amount):
        fee = amount * 0.03
        print(f"EasyPaisa Payment: {amount} Fee: {fee}")


class NayaPay(PaymentGateway):

    def process_payment(self, amount):
        fee = amount * 0.01
        print(f"NayaPay Payment: {amount} Fee: {fee}")


gateway = JazzCash()
gateway.process_payment(5000)

gateway = EasyPaisa()
gateway.process_payment(5000)
gateway = NayaPay()
gateway.process_payment(5000)