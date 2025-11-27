from payment_method import PaymentMethod

class DefaultPayment(PaymentMethod):
    def pay(self, amount):
        print(f"Payment successful: {amount}₸")
        return True
