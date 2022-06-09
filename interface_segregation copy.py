import abc


class PaymentProcessor(abc.ABC):
    
    @abc.abstractmethod
    def pay(self):
        pass

    @abc.abstractmethod
    def authorize_2fa(self):
        pass

class PaypalPaymentProcessor(PaymentProcessor):
    
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

    def authorize_2fa(self):
        raise ValueError("does not support 2fa")

