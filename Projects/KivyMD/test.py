from kivy.lang import Builder
from kivymd.app import MDApp

class MainApp(MDApp):
  def build(self):
    self.theme_cls.theme_style = "Dark"
    self.theme_cls.primary_palette = "BlueGray"
    return Builder.load_file('convert.kv')

  def btn(self):
    self.root.ids.result.text = 'HELLO'
    # self.root.ids.result.text = f'{initial_amount} {fromCurr} = {amount:.2f} {toCurr}'
  
MainApp().run()