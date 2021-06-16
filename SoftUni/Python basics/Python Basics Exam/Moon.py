import math

distance_to_moon = 384400
time_spent = 3

speed = float(input())
fuel = float(input())

total_distance = distance_to_moon * 2
total_time = math.ceil(total_distance / speed + time_spent)
total_fuel = fuel * total_distance/100
print(int(total_time))
print(int(total_fuel))
