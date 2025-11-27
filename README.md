@startuml
class Product {
  - id: int
  - name: string
  - price: float
  + getInfo(): string
}

class Customer {
  - id: int
  - name: string
  - email: string
  + addToCart(product: Product, qty: int)
  + placeOrder(): Order
}

class ShoppingCart {
  - items: List<CartItem>
  + addItem(product: Product, qty: int)
  + removeItem(product: Product)
  + getTotal(): float
}

class CartItem {
  - product: Product
  - quantity: int
  + getSubtotal(): float
}

class Order {
  - id: int
  - items: List<CartItem>
  - total: float
  + calculateTotal(): float
}

class Payment {
  - orderId: int
  - amount: float
  + pay(): bool
}

Customer --> ShoppingCart
ShoppingCart --> CartItem
CartItem --> Product
Customer --> Order
Order --> Payment
@enduml
