class Payment:
    def __init__(self, order_id, amount):
        self.order_id = order_id
        self.amount = amount

    def pay(self):
        print(f"Payment of {self.amount}₸ for order {self.order_id} completed.")
        return True
