import requests
from kivy.lang import Builder
from kivy.properties import StringProperty
# from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp
from kivymd.material_resources import dp
from kivymd.uix.list import OneLineIconListItem
from kivymd.uix.menu import MDDropdownMenu

# Prepares a list of currencies via the API
currencies = f"https://free.currconv.com/api/v7/currencies?apiKey=fe444f880c2cb85b3f6a"
data = requests.get(currencies).json()['results']
rates = []
currency = {}

for k, v in data.items():
    currency[k] = v['currencyName']
    rates.append(f"{k} - {v['currencyName']}")
rates.sort()

class OneLineListItem(OneLineIconListItem):
    text = StringProperty()


class Test(MDApp):
    # Build the App
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # self.rates = rates
        self.screen = Builder.load_file("test.kv")

        # Sets the items in the from_currency menu
        menu_items = [
            {
                "viewclass": "OneLineListItem",
                "icon": "cash",
                "text": rate,
                "height": dp(40),
                "on_release": lambda x=rate: self.from_currency(x)} for rate in rates
        ]

        # this is called when you click on the text field -- it is a reference to "on_focus" caller in .kv file
        self.menu_from_currency = MDDropdownMenu(
            caller=self.screen.ids.from_currency,
            items=menu_items,
            position="bottom",
            width_mult=4,
        )

        # Sets the items in the to_currency menu
        menu_items = [
            {
                "viewclass": "OneLineListItem",
                "icon": "cash",
                "text": rate,
                "height": dp(40),
                "on_release": lambda x=rate: self.to_currency(x)} for rate in rates
        ]

        # this is called when you click on the text field -- it is a reference to "on_focus" caller in .kv file
        self.menu_to_currency = MDDropdownMenu(
            caller=self.screen.ids.to_currency,
            items=menu_items,
            position="bottom",
            width_mult=4,
        )

    # the function place the selected text in the text field
    def from_currency(self, text_item):
        self.screen.ids.from_currency.text = text_item
        self.menu_from_currency.dismiss()

    # the function place the selected text in the text field
    def to_currency(self, text_item):
        self.screen.ids.to_currency.text = text_item
        self.menu_to_currency.dismiss()

    # Function for the button
    def btn(self):

      # takes first three letters from the currency
      from_currency = self.screen.ids.from_currency.text[0:3]  
      to_currency = self.screen.ids.to_currency.text[0:3]

      # takes the amount from the field
      amount = self.screen.ids.amount.text # self.screen.ids.amount.text is a <str>

      # checks the amount to be int or float and if the user has selected something from the drop-down
      if from_currency in currency and to_currency in currency and amount.replace(".", "", 1).isdigit():
        initial_amount = float(amount)
        amount = float(amount)
        url = f'https://free.currconv.com/api/v7/convert?q={from_currency}_{to_currency}&compact=ultra&apiKey=fe444f880c2cb85b3f6a'
        rate = requests.get(url).json()[f"{from_currency}_{to_currency}"]
        amount = round(amount * rate, 2)
        self.root.ids.result.text = f'{initial_amount} {from_currency} = {amount:.2f} {to_currency}'  

      else:
        if from_currency not in currency or to_currency not in currency:
          self.root.ids.result.text = 'Enter a valid three letter currency'
          
        # checks if the user has entered amount
        if not amount.replace(".", "", 1).isdigit():
          self.root.ids.result.text = 'Enter a valid amount'

      # # clears the text input after submit button is clicked
      # self.root.ids.from_currency.text = "From currency"
      # self.root.ids.to_currency.text = "To currency"
      # self.root.ids.amount.text = ""

     
    def build(self):
        self.theme_cls.primary_palette = "LightGreen"
        # self.theme_cls.theme_style = 'Dark'
        return self.screen
        # return Builder.load_file("Projects/KivyMD/test.kv")


if __name__ == "__main__":
    Test().run()
