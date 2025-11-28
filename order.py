from customer import Customer
from coffee import Coffee

class Order:
    all_orders = []

    def __init__(self, customer, coffee, price):
        if not isinstance(customer, Customer):
            raise ValueError("customer must be a Customer instance")
        if not isinstance(coffee, Coffee):
            raise ValueError("coffee must be a Coffee instance")
        
        if not (isinstance(price, (int, float))):
            raise ValueError("price must be a number")
        price = float(price)
        if not (1.0 <= price <= 10.0):
            raise ValueError("price must be between 1.0 and 10.0")
        
        self.customer = customer
        self.coffee = coffee
        self.price = price

        Order.all_orders.append(self)

    def __str__(self):
        return f"{self.customer.name} bought {self.coffee.name} at {self.price}"
    
#o = Order("alice", "latte", 3.5)
#print(o)
