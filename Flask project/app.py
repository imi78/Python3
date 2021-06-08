import requests
from flask import Flask, render_template, request
app = Flask(__name__)

currencies = f"https://free.currconv.com/api/v7/currencies?apiKey=fe444f880c2cb85b3f6a"
rates = requests.get(currencies).json()['results']

@app.route('/', methods=['GET', 'POST'])
def index():

    if request.method == "POST":
        from_currency = request.form["from_currency"]
        to_currency = request.form["to_currency"]
        amount = request.form["amount"]
        url = f'https://free.currconv.com/api/v7/convert?q={from_currency}_{to_currency}&compact=ultra&apiKey=fe444f880c2cb85b3f6a'
        rate = requests.get(url).json()[f"{from_currency}_{to_currency}"]
        amount = int(amount)
        initial_amount = amount
        amount = round (amount * rate, 2)
        return render_template('index.html', rates=rates, result=f'{initial_amount} {from_currency} = {amount} {to_currency}')

    return render_template('index.html', rates=rates)