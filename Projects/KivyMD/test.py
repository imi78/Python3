from kivymd.app import MDApp
from kivymd.material_resources import dp
from kivymd.uix.menu import MDDropdownMenu
from kivy.lang import Builder
from kivy.clock import Clock
from kivymd.uix.screen import Screen


class MainApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.screen = Builder.load_file("test.kv")

        menu_items = [
            {
                "viewclass": "MDDropDownItem",
                "icon": "git",
                "text": f"Item {i}",
                "height": dp(56),
                "on_release": lambda x=f"Item {i}": self.set_item(x),
            } for i in range(5)
        ]
        self.menu = MDDropdownMenu(
            caller=self.screen.ids.from_currency,
            items=menu_items,
            position="center",
            width_mult=4,
        )
        self.menu.bind()

    def set_item(self, text_item):
        self.screen.ids.from_currency.set_item(text_item)
        self.menu.dismiss()

    def build(self):

        self.theme.cls.primary_palette = "BlueGray"
        self.theme.cls.theme_style = "Dark"

        return self.screen


if __name__ == "__main__":
    MainApp().run()
