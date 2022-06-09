import abc


class PaymentProcessor(abc.ABC):
    
    def pay(self):
        pass

class PaypalPaymentProcessor(PaymentProcessor):
    
    def __init__(self, dollars, order):
        self.dollars = dollars
        self.order = order

    def pay(self):
        pass

class CreditCardPaymentProcessor(PaymentProcessor):

    def __init__(self, dollars, order):
        self.dollars = dollars
        self.order = order
    
    def pay(self):
        pass

class BitcoinPaymentProcessor(PaymentProcessor):

    def __init__(self, bitcoins, order):
        self.bitcoins = bitcoins
        self.order = order
    
    def pay(self):
        pass

