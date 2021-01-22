class Vehicle:
    def __init__(self, car_type, car_model, car_price):
        self.type = car_type
        self.model = car_model
        self.price = car_price
        self.owner = None

    def buy(self, money, owner):
        if self.owner is not None:
            print("Car already sold")
        if money >= self.price and self.owner is None:
            self.owner = owner
            print(f"Successfully bought a {self.type}. Change: {abs(money - self.price):.2f}")
        if money < self.price:
            print("Sorry, not enough money")

    def sell(self):
        if self.owner is not None:
            self.owner = None
        else:
            print("Vehicle has no owner")

    def __repr__(self):
        if self.owner is not None:
            return f'{self.model} {self.type} is owned by: {self.owner}'
        else:
            return f'{self.model} {self.type} is on sale: {self.price}'


vehicle_type = "car"
model = "BMW"
price = 30000
vehicle = Vehicle(vehicle_type, model, price)
vehicle.buy(15000, "Peter")
vehicle.buy(30000, "George")
vehicle.buy(35000, "Ivo")
print(vehicle)
vehicle.sell()
vehicle.buy(35000, "Ivo")
print(vehicle)

