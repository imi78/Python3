import requests
from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    url = 'http://data.fixer.io/api/latest?access_key=c1bf0b4af0dd8939a2da6c80e10c5bbf'
    data = requests.get(url).json()
    rates = data['rates']
    return render_template("index.html", rates=rates)
    
@app.route('/', methods =["GET", "POST"])
def 
