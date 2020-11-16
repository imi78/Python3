days = int(input())
hours = int(input())
price = 0

for day in range(1, days + 1):
  for hour in range(1, hours + 1):
    if day % 2 == 0 and hour % 2 == 1:
      price += 2.50
    elif day % 2 == 1 and hour % 2 == 0:
      price += 1.25
    else: 
      price += 1
print (price:.2f)