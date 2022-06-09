import abc


class PaymentProcessor(abc.ABC):
    
    @abc.abstractmethod
    def pay(self):
        pass

class PaymentProcess2fa(PaymentProcessor):

    def authorize_2fa(self):
        pass

class SMSAuth:

    authorized = False

    def verify(self, code):
        pass

    def is_authorized(self):
        return self.authorized

class YubukeyAuth:
    
    authorized = False

    def verify(self, code):
        pass

    def is_authorized(self):
        return self.authorized



class PaypalPaymentProcessor(PaymentProcess2fa):
    
    def __init__(self, dollars, order, authorizer: SMSAuth):
        self.dollars = dollars
        self.order = order
        authorizer = authorizer

    def pay(self):
        pass

    def authorize_2fa(self):
        pass

auth = SMSAuth()
x = PaypalPaymentProcessor(100, 'xyz', auth)

