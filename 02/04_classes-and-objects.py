# Complete implementation of three methods
# 
#  __init__ should take an argument "name". It should initialize self.name to the argument and self.items to be an empty list
#
# add_item should append a dictionary representing an item to the store's items property. The dictionary should have keys name and price.
#
# stock_price should add up each item price inside self.items to come up with a total and return that

class Store:
    def __init__(self, name):
        self.name = name
        self.items = []

    def add_item(self, name, price):
        self.items.append({'name': name, 'price': price})

    def stock_price(self):
        return sum([x['price'] for x in self.items])



if __name__ == "__main__":
    s = Store("Tom's Hardware Store")
    s.add_item('Hammer', 10.5)
    s.add_item('Nails', 2.3)
    s.add_item('Wooden plank', 5.0)
    print(f"Tom's Hardware store total: {s.stock_price()}")
