food = float(1)*1000
hay = float(1.5)*1000
cover = float(3)*1000
weight = float(1.5)*1000
day = 1

while day <= 30:
    food -= 300.00
    if day % 2 == 0:
        hay -= food * 0.05
    if day % 3 == 0:
        quantity = round(weight/3, 2)
        cover -= quantity
    day +=1
    if food < 0 or hay < 0 or cover < 0:
        break
    
if food > 0 and hay > 0 and cover > 0:
    print(f"Everything is fine! Puppy is happy! Food: {food/1000:.2f}, Hay: {hay/1000:.2f}, Cover: {cover/1000:.2f}.")
else:
    print(f"Merry must go to the pet store! Food is enough for {day-1} days")
   
