import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty


class Grid(Widget):  # this is "root"
  name = ObjectProperty(None)
  e_mail = ObjectProperty(None)

  def btn(self):
    print(self.name.text, self.e_mail.text)
    self.name.text = "" # cleares the text input after submit button is clicked
    self.e_mail.text = ""

 
class Convert(App):
  def build(self):
    return Grid()


if __name__ == "__main__":
    Convert().run()
