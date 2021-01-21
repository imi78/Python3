class Storage:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = []

    def add_product(self, product):
        if self.capacity > len(self.storage):
            self.storage.append(product)
        return self.storage

    def get_products(self):
        return self.storage


storage = Storage(4)
storage.add_product('Apple')
storage.add_product('Banana')
storage.add_product('Apricot')
storage.add_product('Plum')
storage.add_product('Pear')
print(storage.get_products())