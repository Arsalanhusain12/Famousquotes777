from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperties
from kivy.core.window import Wondow

window.size=(500,700)

Builder.load_file('calc.kv')

class MyLayout(Widget):
       pass
       
class CalculatorApp(App):
       def build(self):
             return MyLayout()
             
if __name__== '__main__':
    CalculatorApp().run()                          