class CustomerOrder:

    def add_to_order(self, item):
        pass

    def total(self):
        pass

class PaymentProcessor:

    def __init__(self, order):
        self.order = order

    def pay(self, amount):
        pass


order = CustomerOrder()
order.add_to_order("some_item")

payment_processor = PaymentProcessor(order)
payment_processor.pay(order.total)





    

