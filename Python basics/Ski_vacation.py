days = int(input())
days_of_stay = days-1
suite = input()
grade = input()

room = 18.00
apartment = 25.00
president_apartment = 35.00
price = 0
if suite == 'room for one person':
    discount = 0
    price = days_of_stay * room - discount

elif suite == 'apartment':
    if days_of_stay < 10:
        discount = days_of_stay * apartment * 0.30
        price = days_of_stay * apartment - discount

    elif 10 <= days_of_stay <= 15:
        discount = days_of_stay * apartment * 0.35
        price = days_of_stay * apartment - discount

    elif days_of_stay > 15:
        discount = days_of_stay * apartment * 0.50
        price = days_of_stay * apartment - discount

elif suite == 'president apartment':

    if days_of_stay < 10:
        discount = days_of_stay * president_apartment * 0.10
        price = days_of_stay * president_apartment - discount

    elif 10 <= days_of_stay <= 15:
        discount = days_of_stay * president_apartment * 0.15
        price = days_of_stay * president_apartment - discount

    elif days_of_stay > 15:
        discount = days_of_stay * president_apartment * 0.20
        price = days_of_stay * president_apartment - discount

if grade == 'positive':
    price += price * 0.25

elif grade == 'negative':
    price -= price * 0.10

print(f'{price:.2f}')