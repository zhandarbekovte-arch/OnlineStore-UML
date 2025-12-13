## UML Class Diagram (Mermaid)

```mermaid
classDiagram
    class Product {
        -id
        -name
        -price
        +get_info()
    }

    class CartItem {
        -product
        -quantity
        +get_subtotal()
    }

    class ShoppingCart {
        -items
        +add_item()
        +remove_item()
        +get_total()
    }

    class Order {
        -id
        -items
        -total
        +calculate_total()
    }

    class PaymentMethod {
        <<interface>>
        +pay(amount)
    }

    class DefaultPayment {
        +pay(amount)
    }

    class Customer {
        -id
        -name
        -email
        -cart
        +add_to_cart()
        +place_order()
    }

    Customer --> ShoppingCart
    ShoppingCart --> CartItem
    CartItem --> Product
    Customer --> Order
    Order --> CartItem
    Customer --> PaymentMethod : uses
    PaymentMethod <|.. DefaultPayment
