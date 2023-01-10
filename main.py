from kivymd.app import MDApp
from kivymd.uix.label import MDLabel

class CalculatorApp(MDApp):
    def build(self):
        return MDLabel(text = 'Calculator', pos_hint = {'center_x': 1, 'center_y': 0.5})

CalculatorApp().run()