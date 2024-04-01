import requests
from flask import Flask, render_template, request, flash, url_for, redirect
app = Flask(__name__)

app.secret_key = 'SECRET_KEY'

currencies = f"https://free.currconv.com/api/v7/currencies?apiKey=cef015474ccc6be8380a"

data = requests.get(currencies).json()['results']

rates = []
for v in data.values():
  rates.append(f"{v['id']} -  {v['currencyName']}")
rates.sort()

@app.route('/', methods=['GET', 'POST'])
def index():

    if request.method == "POST":
        from_currency = request.form["from_currency"]
        to_currency = request.form["to_currency"]
        amount = request.form["amount"]
        if from_currency != "From currency" and to_currency != "To currency" and amount != "":
            amount = float(amount)
            initial_amount = amount
            url = f'https://free.currconv.com/api/v7/convert?q={from_currency}_{to_currency}&compact=ultra&apiKey=cef015474ccc6be8380a'
            rate = requests.get(url).json()[f"{from_currency}_{to_currency}"]
            amount = round (amount * rate, 2)
            return render_template('index.html', rates=rates, result=f'{initial_amount} {from_currency} = {amount} {to_currency}')
        else:
            flash("Holy guacamole! You should pick currency.")
            return redirect(url_for('index'))

    return render_template('index.html', rates=rates)
