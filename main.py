import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.uix.floatlayout import FloatLayout


class Grid(Widget):  # this is accessible by "root." not by "Grid."
    fromCurr = ObjectProperty(None)
    toCurr = ObjectProperty(None)

    def btn(self):
        print(f"{self.fromCurr.text} - {self.toCurr.text}")
        
        self.fromCurr.text = ""  # cleares the text input after submit button is clicked
        self.toCurr.text = ""


class Convert(App):
    def build(self):
        return Grid()


if __name__ == "__main__":
    Convert().run()
