import abc


class PaymentProcessor(abc.ABC):
    
    def __init__(self, order):
        self.order = order

    @abc.abstractmethod
    def pay(self, amount):
        pass

class PaypalPaymentProcessor(PaymentProcessor):
    
    def pay(self, amount):
        pass

class CreditCardPaymentProcessor(PaymentProcessor):
    
    def pay(self, amount):
        pass

    


