budget = float(input())
season = input()

if budget <= 100:
    if season == 'summer':
        place = 'Bulgaria'
        rest_type = 'Camp'
        price = budget*0.30
    elif season == 'winter':
        place = 'Bulgaria'
        rest_type = 'Hotel'
        price = budget*0.70

if 100 < budget <= 1000:
    if season == 'summer':
        place = 'Balkans'
        rest_type = 'Camp'
        price = budget*0.40
    elif season == 'winter':
        rest_type = 'Hotel'
        place = 'Balkans'
        price = budget*0.80

elif budget > 1000:
    place = 'Europe'
    rest_type = 'Hotel'
    price = budget*0.90

print (f'Somewhere in {place} \n {rest_type} - {price:.2f}')