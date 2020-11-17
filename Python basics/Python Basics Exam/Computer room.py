month = input()
hours = int(input())
group = int(input())
time_of_day = input()
price = 0

if time_of_day == 'day':
    if month == 'march' or month == 'april' or month == 'may':
        price = 10.50
    elif month == 'june' or month == 'july' or month == 'august':
        price = 12.60

elif time_of_day == 'night':
    if month == 'march' or month == 'april' or month == 'may':
        price = 8.40
    elif month == 'june' or month == 'july' or month == 'august':
        price = 10.20
if group >= 4:
    price -= price * 0.10
if hours >= 5:
    price -= price * 0.50

print(f'Price per person for one hour: {price:.2f}')
print(f'Total cost of the visit: {price * hours * group:.2f}')
