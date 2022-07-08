n = int(input())

for i in range(n):
    car,mileage,fuel = input().split("|")
    mileage,fuel = map(int,(mileage,fuel))



while True:
    command, car, distance, fuel = input().lower().split(" : ")
    distance, fuel = map(int,(distance, fuel))
    
    if command == 'stop':
        break
    
    if command == "drive":
        pass
    
    if command == "refuel":
        pass
    
    if command == "revert":
        pass