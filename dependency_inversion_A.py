import abc


class PaymentProcessor(abc.ABC):
    
    def pay(self):
        pass

class PaymentProcess2fa(PaymentProcessor):

    def authorize_2fa(self):
        pass

class Auth(abc.ABC):

    @abc.abstractmethod
    def is_authorized(self):
        pass

class SMSAuth(Auth):

    authorized = False

    def verify(self, code):
        pass

    

    
class YubukeyAuth(Auth):
    
    authorized = False

    def verify(self, code):
        pass

    def is_authorized(self):
        return self.authorized



class PaypalPaymentProcessor(PaymentProcess2fa):
    
    def __init__(self, dollars, order, authorizer: Auth):
        self.dollars = dollars
        self.order = order
        authorizer = authorizer

    def pay(self):
        pass

    def authorize_2fa(self):
        pass

auth = YubukeyAuth()
x = PaypalPaymentProcessor(100, 'xyz', auth)



