class Car:
  owner = None
  def __init__(self, car_type, model, price):
    self.car_type = car_type
    self.model = model
    self.price = price
    self.owner = None

  def buy(self, money, owner):
    self.money = money

    if self.money >= self.price and self.owner == None:
        self.owner = owner
        print(f"Successfully bought a {self.car_type}. Change: {self.money-self.price}")
        
    elif self.money < self.price:
      print("Sorry, not enough money")
      
    elif self.owner != None:
      print("Car already sold")
      
  def sell(self):
    if self.owner != None:
      self.owner = None
    else:
      print("Vehicle has no owner")

  def __repr__(self):
      
      if self.owner != None:
          return f"{self.model} {self.car_type} is owned by: {self.owner}" 
      else:
          return f"{self.model} {self.car_type} is on sale: {self.price}"
          
    
    
vehicle_type = "truck"
model = "Scania"
price = 10000
vehicle = Car(vehicle_type, model, price)
vehicle.buy(15000, "Peter")
vehicle.buy(35000, "George")
print(vehicle)
vehicle.sell()
print(vehicle)
