import requests
# import kivy
from kivy.app import App
# from kivy.uix.label import Label
# from kivy.uix.gridlayout import GridLayout
# from kivy.uix.textinput import TextInput
# from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.properties import StringProperty
# from kivy.uix.floatlayout import FloatLayout
# from kivy.uix.dropdown import DropDown
# from kivy.base import runTouchApp

currencies = f"https://free.currconv.com/api/v7/currencies?apiKey=fe444f880c2cb85b3f6a"
data = requests.get(currencies).json()['results']
currency = []

for k, v in data.items():
    currency.append(f"{v['id']} -  {v['currencyName']}")
currency.sort()


class Grid(Widget):  # this is accessible by "root." not by "Grid."
    fromCurr = ObjectProperty(None)
    toCurr = ObjectProperty(None)
    amount = ObjectProperty(None)
    result = StringProperty('')  # sets the result variable
    currency = currency  # put list here so it can be accessible by root.

    def btn(self):  # function for conversion
        fromCurr = self.fromCurr.text[0:3]  # takes first three letters from the curency
        toCurr = self.toCurr.text[0:3]
        amount = self.amount.text  # self.amout.text is a <str>

        if fromCurr in currency and toCurr in currency and amount.isdigit():
            initial_amount = int(amount)
            amount = float(amount)
            url = f'https://free.currconv.com/api/v7/convert?q={fromCurr}_{toCurr}&compact=ultra&apiKey=fe444f880c2cb85b3f6a'
            rate = requests.get(url).json()[f"{fromCurr}_{toCurr}"]
            amount = round(amount * rate, 2)
            self.result = f'{initial_amount} {fromCurr} = {amount:.2f} {toCurr}'  # can be accessed in kv file by root.result

        else:
            if fromCurr not in currency or toCurr not in currency:
                self.result = 'Enter a valid three letter currency'
            if amount.isdigit() == False:
                self.result = 'Enter a valid amount'

            self.fromCurr.text = "From currency"  # cleares the text input after submit button is clicked
            self.toCurr.text = "To currency"


class Convert(App):
    def build(self):
        return Grid()


if __name__ == "__main__":
    Convert().run()
