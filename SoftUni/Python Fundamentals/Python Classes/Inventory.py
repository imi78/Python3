class Inventory:
    __capacity = None

    def __init__(self, capacity):
        # self.capacity = capacity  # ????
        Inventory.__capacity = capacity  # ????
        self.items = []

    def add_item(self, item):
        if len(self.items) < Inventory.__capacity:
            self.items.append(item)
        else:
            return 'not enough room in the inventory'

    def get_capacity(self):
        return Inventory.__capacity

    def __repr__(self):
        return f"Items: {', '.join(self.items)}.\nCapacity left: {Inventory.__capacity - len(self.items)}"


inventory = Inventory(2)
inventory.add_item("potion")
inventory.add_item("sword")
print(inventory.add_item("bottle"))
print(inventory.get_capacity())
print(inventory)
