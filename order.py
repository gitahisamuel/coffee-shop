from customer import Customer;
from coffee import Coffee;

class Order:
    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price


    def __init__(self):
        pass    


customer = Customer()
coffee = Coffee()