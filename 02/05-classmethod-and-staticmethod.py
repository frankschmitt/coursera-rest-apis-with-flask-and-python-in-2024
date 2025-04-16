# complete two method implementations
# 
# 1. franchise: takes a store as argument, returns a new Store object with name equal to the argument + " - franchise".
# 2. store_details: also takes a store as argument, should return string representing the argument

class Store:
    def __init__(self, name):
        self.name = name
        self.items = []

    def add_item(self, name, price):
        self.items.append({'name': name, 'price': price})

    def stock_price(self):
        return sum([item['price'] for item in self.items])

    @classmethod
    def franchise(cls, store):
        pass

    @classmethod
    def store_details(store):
        pass
