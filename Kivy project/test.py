import kivymd
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivymd.toast import toast
from kivymd.app import MDApp
from kivymd.uix.menu import MDDropdownMenu

# .kv file design
Builder.load_file("test.kv")

class Convert(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.screen = Builder.load_string()
        menu_items = [{"text": f"Item {i}"} for i in range(5)]
        self.menu = MDDropdownMenu(
            caller=self.screen.ids.dropdown_item,
            items=menu_items,
            position="center",
            width_mult=4,
        )
        self.menu.bind(on_release=self.set_item)

    def set_item(self, instance_menu, instance_menu_item):
        self.screen.ids.dropdown_item.set_item(instance_menu_item.text)
        instance_menu.dismiss()

    def build(self):
        return self.screen


Convert().run()
