from kivymd.app import MDApp
from kivymd.uix.button import MDTextButton
from kivymd.uix.gridlayout import MDGridLayout

class TestApp (MDApp):
    def build(self):
        bl = MDGridLayout(pos_hint = {'centr_x':0.5 , 'center_y':0.5} , cols = 3 , rows = 4 , padding = 50 , spacing = 50)
        lab = MDTextButton(text = '1')
        lab1 = MDTextButton(text = '2')
        lab2 = MDTextButton(text = '3')
        lab3 = MDTextButton(text = '4')
        lab4 = MDTextButton(text = '5')
        lab5 = MDTextButton(text = '6')
        lab6 = MDTextButton(text = '7')
        lab7 = MDTextButton(text = '8')
        lab8 = MDTextButton(text = '9')
        lab9 = MDTextButton(text = '0')
        bl.add_widget(lab)
        bl.add_widget(lab1)
        bl.add_widget(lab2)
        bl.add_widget(lab3)
        bl.add_widget(lab4)
        bl.add_widget(lab5)
        bl.add_widget(lab6)
        bl.add_widget(lab7)
        bl.add_widget(lab8)
        bl.add_widget(lab9)
        return bl

if __name__ == '__main__':
    TestApp().run()
