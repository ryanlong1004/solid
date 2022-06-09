import abc


class PaymentProcessor(abc.ABC):
    
    def pay(self):
        pass

class PaymentProcess2fa(PaymentProcessor):

    def authorize_2fa(self):
        pass

class PaypalPaymentProcessor(PaymentProcess2fa):
    
    def __init__(self, dollars, order):
        self.dollars = dollars
        self.order = order

    def pay(self):
        pass

    def authorize_2fa(self):
        pass

class CreditCardPaymentProcessor(PaymentProcessor):

    def __init__(self, dollars, order):
        self.dollars = dollars
        self.order = order
    
    def pay(self):
        pass


