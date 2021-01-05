class Storage:

  def __init__(self, capacity):
    self.capacity = capacity
    self.storage = []


  def add_product(self, product):
    if len(self.storage) < self.capacity:
      self.storage.append(product)

  def get_products(self):
    return self.storage


storage = Storage(3)
storage.add_product('apple')
storage.add_product('banana')
storage.add_product('bread')
storage.add_product('tomato')
print(storage.get_products())