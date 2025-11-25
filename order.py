from customer import Customer;
from coffee import Coffee;

class Order:
    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price


customer = Customer()
coffee = Coffee()