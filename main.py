import requests
url = 'http://data.fixer.io/api/latest?access_key=c1bf0b4af0dd8939a2da6c80e10c5bbf'
data = requests.get(url).json()
rates = {}


def convert(from_currency, to_currency, amount):   
    initial_amount = amount
    rates = data['rates']
    if from_currency != 'EUR':
        amount = amount / rates[from_currency]  # calculates the base currency (EUR) rate.

    amount = round(amount * rates[to_currency], 2)  # then re-calculates the rate to the given currency
    print(f'{initial_amount} {from_currency} = {amount:.2f} {to_currency}')

from_currency = input("From currency: ").upper()
to_currency = input("To currency: ").upper()
amount = int(input("Amount: "))

   
convert(from_currency, to_currency, amount)
