from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp
from kivymd.material_resources import dp
from kivymd.uix.list import OneLineIconListItem
from kivymd.uix.menu import MDDropdownMenu


class IconListItem(OneLineIconListItem):
    icon = StringProperty()


class Test(MDApp):
    # Build the App
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.screen = Builder.load_file("Projects/KivyMD/test.kv")

        # Sets the items in the from_currency menu
        menu_items = [
            {
                "viewclass": "IconListItem",
                "icon": "git",
                "text": f"Item {i}",
                "height": dp(56),
                "on_release": lambda x=f"Item {i}": self.from_currency(x),
            } for i in range(5)
        ]

        # this is called when you click on the text field -- it is a reference to "on_focus" caller
        self.menu_from_currency = MDDropdownMenu(
            caller=self.screen.ids.from_currency,
            items=menu_items,
            position="bottom",
            width_mult=4,
        )

        # Sets the items in the to_currency menu
        menu_items = [
            {
                "viewclass": "IconListItem",
                "icon": "git",
                "text": f"Item {i}",
                "height": dp(56),
                "on_release": lambda x=f"Item {i}": self.to_currency(x),
            } for i in range(5)
        ]

        # this is called when you click on the text field -- it is a reference to "on_focus" caller
        self.menu_to_currency = MDDropdownMenu(
            caller=self.screen.ids.to_currency,
            items=menu_items,
            position="bottom",
            width_mult=4,
        )

    # the function place the selected text int he text field
    def from_currency(self, text_item):
        self.screen.ids.from_currency.text = text_item
        self.menu_from_currency.dismiss()

    # the function place the selected text int he text field
    def to_currency(self, text_item):
        self.screen.ids.to_currency.text = text_item
        self.menu_to_currency.dismiss()

    # Function for the button
    def btn(self):
        self.root.ids.result.text = f"HELLO {self.root.ids.result.text}"

    def build(self):
        self.theme_cls.primary_palette = "Gray"
        self.theme_cls.theme_style = 'Dark'
        return self.screen
        # return Builder.load_file("Projects/KivyMD/test.kv")


if __name__ == "__main__":
    Test().run()
