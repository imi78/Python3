n = int(input())
cars = []
for i in range(n):
    car,mileage,fuel = input().split("|") # split the string
    mileage,fuel = map(int,(mileage,fuel)) # map to int
    
    # append everything as nested list
    cars.append(([car,mileage,fuel]))


while True:
    
    # *other receives unknown number of items, in this case distance, fuel or just fuel
    command, *other = input().split(" : ")
    
    # First check if the command is 'Stop'
    if command == 'Stop':
        for car in cars:
            print(f"{car[0]} -> Mileage: {car[1]} kms, Fuel in the tank: {car[2]} lt.")
        break
    # we assign the first value to a 'car' variable and remove it from the list.
    car = other.pop(0)
    
    # convert the rest of the elements into integer(s)
    other = [int(x) for x in other]
    
    # assign the elements from the list into variables
    if len(other) == 2:
       distance = other[0]
       fuel = other[1]
       
    else:
        fuel = other[0]
        # variable for 'Revert'
        kilometers = other[0]
    
    if command == "Drive":
        for i in cars:
            if car in i:
                if fuel <= i[2]:
                    i[1] += distance
                    i[2] -= fuel
                    print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
                else:
                    print("Not enough fuel to make that ride")
                    
    # Each car can have only 75lt. of fuel
    if command == "Refuel":
        for i in cars:
            # checks if this is the requested car
            if car in i:
                # checks the fuel level
                if (i[2] + fuel) > 75:
                    print(f"{car} refueled with {75 - i[2]} liters")
                    i[2] = 75                 
                else:
                    print(f"{car} refueled with {fuel} liters")
                    i[2] += fuel
    
    if command == "Revert":
        for i in cars:
            if car in i:
                if i[1] < 10000 or (i[1] - kilometers < 10000):
                    i[1] = 10000
                else:
                    i[1] -= kilometers
                    print(f"{car} mileage decreased by {kilometers} kilometers")