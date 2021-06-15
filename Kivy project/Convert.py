import requests
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty

currencies = f"https://free.currconv.com/api/v7/currencies?apiKey=fe444f880c2cb85b3f6a"
data = requests.get(currencies).json()['results']
rates = []

class Grid(Widget):  # this is accessible by "root." not by "Grid."
    fromCurr = ObjectProperty(None)
    toCurr = ObjectProperty(None)
    amount  = ObjectProperty(None)

    def btn(self):  # function for conversion 
       
        amount = self.amount.text  # self.amout.text is a <str>
        if self.fromCurr in rates and self.toCurr in rates and amount.isdigit():
          initial_amount = int(amount)
          amount = amount / rates[self.fromCurr]  # calculates the base currency (EUR) rates
          amount = round(amount * rates[self.toCurr], 2)  # then re-calculates the rate to the given currency
          print(f'{initial_amount} {self.fromCurr} = {amount:.2f} {self.toCurr}')
        else:
          if self.fromCurr not in rates or self.toCurr not in rates:
            print('Enter a valid three letter currency')
          if amount.isdigit() == False:
            print('Enter a valid amount')
        
        # self.fromCurr.text = ""  # cleares the text input after submit button is clicked
        # self.toCurr.text = ""


class Convert(App):
    def build(self):
        return Grid()


if __name__ == "__main__":
    Convert().run()
