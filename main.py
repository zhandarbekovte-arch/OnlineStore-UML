from product import Product
from customer import Customer
from default_payment import DefaultPayment

p1 = Product(1, "Laptop", 350000)
p2 = Product(2, "Mouse", 5000)

customer = Customer(1, "Yersin", "test@example.com")

customer.add_to_cart(p1, 1)
customer.add_to_cart(p2, 2)

payment = DefaultPayment()   # Төлем түрі
order = customer.place_order(payment)

print("Order total:", order.total)
