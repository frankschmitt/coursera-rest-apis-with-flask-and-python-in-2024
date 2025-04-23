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

    def __repr__(self):
        return f"{self.name}, total stock price: {self.stock_price()}"

    @classmethod
    def franchise(cls, store):
        return Store(store.name + " - franchise")

    @classmethod
    def store_details(cls, store):
        return str(store)



if __name__ == "__main__":
    s = Store("Tom's Hardware Store")
    s.add_item('Hammer', 10.5)
    s.add_item('Nails', 2.3)
    s.add_item('Wooden plank', 5.0)
    print(f"Tom's Hardware store total: {s.stock_price()}")
    print(f"details: {Store.store_details(s)}")
    s2 = Store.franchise(s)
    print(f"franchise store: {s2}")
