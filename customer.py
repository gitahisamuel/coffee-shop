# customer.py

from order import Order
from coffee import Coffee

class Customer:
    def __init__(self, name: str):
        if not isinstance(name, str):
            raise ValueError("Customer name must be a string")
        if not (1 <= len(name) <= 15):
            raise ValueError("Customer name must be between 1 and 15 characters")
        self.name = name

    def orders(self):
        return [o for o in Order.all_orders if o.customer == self]

    def coffees(self):
        coffees = [o.coffee for o in self.orders()]
        # eliminate duplicates
        unique = []
        for c in coffees:
            if c not in unique:
                unique.append(c)
        return unique

    def create_order(self, coffee, price: float):
        """Place a new order for this customer."""
        return Order(self, coffee, price)

    @classmethod
    def most_aficionado(cls, coffee):
        """Return the Customer who has spent the most total on the given coffee."""
        totals = {}
        for o in Order.all_orders:
            if o.coffee == coffee:
                totals.setdefault(o.customer, 0.0)
                totals[o.customer] += o.price
        if not totals:
            return None
        # Return the customer with the maximum total spent
        best = max(totals.items(), key=lambda kv: kv[1])
        return best[0]

    def __repr__(self):
        return f"<Customer: {self.name}>"
