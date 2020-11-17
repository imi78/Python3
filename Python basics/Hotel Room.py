month = input()
days_of_stay = int(input())

if month == 'May' or month == 'October':
    price_studio =  50*days_of_stay
    price_apartment = 65*days_of_stay
    if 7 < days_of_stay <= 14:
        price_studio -= price_studio*0.05
    elif days_of_stay >14:
        price_studio -= price_studio * 0.30
        price_apartment -= price_apartment * 0.10

elif month == 'June' or month == 'September':
    price_studio = 75.20 * days_of_stay
    price_apartment = 68.70 * days_of_stay
    if days_of_stay > 14:
        price_studio -= price_studio * 0.20
        price_apartment -= price_apartment * 0.10

elif month == 'July' or month == 'August':
    price_studio = 76*days_of_stay
    price_apartment = 77*days_of_stay
    if days_of_stay > 14:
        price_apartment -= price_apartment * 0.10

print (f'Apartment: {price_apartment:.2f} lv.')
print (f'Studio: {price_studio:.2f} lv.')
