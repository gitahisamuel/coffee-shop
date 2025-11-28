# coffee.py

from order import Order
from customer import Customer

class Coffee:
    def __init__(self, name: str):
        if not isinstance(name, str):
            raise ValueError("Coffee name must be a string")
        if len(name) < 3:
            raise ValueError("Coffee name must be at least 3 characters long")
        self.name = name

    def orders(self):
        """Return list of Order instances for this coffee."""
        return [o for o in Order.all_orders if o.coffee == self]

    def customers(self):
        """Return unique list of Customers who ordered this coffee."""
        custs = [o.customer for o in self.orders()]
        unique = []
        for c in custs:
            if c not in unique:
                unique.append(c)
        return unique

    def num_orders(self):
        """Return total count of orders for this coffee."""
        return len(self.orders())

    def average_price(self):
        """Return the average price paid for this coffee, or None if no orders."""
        os = self.orders()
        if not os:
            return None
        total = sum(o.price for o in os)
        return total / len(os)

    def __repr__(self):
        return f"<Coffee: {self.name}>"
