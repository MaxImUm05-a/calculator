from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDTextButton
from kivymd.uix.gridlayout import MDGridLayout

class MyButton(MDTextButton):
    save = ''

    def __init__(self, text, *args, **kwargs):
        self.text = text
        super().__init__(text = text, *args, **kwargs)

    def on_release(self):
        txt = app.jkl.text

        if self.text in '1234567890.':
            if MyButton.save == '=':
                app.jkl.text = self.text
                MyButton.save = ''
            elif txt in '*/-+':
                app.jkl.text = self.text
            else:
                app.jkl.text = txt + self.text
        elif self.text in '*/+-':
            if txt in '*/+-':
                MyButton.save = MyButton.save[:-1] + self.text
            else:
                MyButton.save = txt + self.text
            app.jkl.text = self.text
        elif self.text == 'C':
            app.jkl.text = ''
        elif self.text == '<=':
            if txt == 'Error':
                app.jkl.text = ''
            else:
                app.jkl.text = txt[:-1]
        elif self.text == '=':
            try:
                app.jkl.text = str(eval(MyButton.save + txt))
            except:
                app.jkl.text = 'Error'
            MyButton.save = '='

class TestApp(MDApp):
    def build(self):
        bl = MDGridLayout(pos_hint = {'centr_x':0.5 , 'center_y':0.5} , cols = 4 , rows = 5 , padding = 50 , spacing = 50)
        df = MDBoxLayout(orientation = 'vertical' , pos_hint = {'center_x':0.5 , 'center_y':0.7} ,  padding = 250 , spacing = 50)
        self.jkl = MDLabel(text = '')
        lab = [MyButton(text=str(x)) for x in range(10)]
        qw = MyButton(text='+')
        qw1 = MyButton(text='-')
        qw2 = MyButton(text='*')
        qw3 = MyButton(text='/')
        qw4 = MyButton(text='=')
        gh = MyButton(text = 'C')
        gh1 = MyButton(text = '<=')
        gh2 = MyButton(text = '.')
        df.add_widget(self.jkl)
        df.add_widget(bl)
        bl.add_widget(gh)
        bl.add_widget(gh1)
        bl.add_widget(qw)
        bl.add_widget(qw1)
        bl.add_widget(lab[1])
        bl.add_widget(lab[2])
        bl.add_widget(lab[3])
        bl.add_widget(qw2)
        bl.add_widget(lab[4])
        bl.add_widget(lab[5])
        bl.add_widget(lab[6])
        bl.add_widget(qw3)
        bl.add_widget(lab[7])
        bl.add_widget(lab[8])
        bl.add_widget(lab[9])
        bl.add_widget(qw4)
        bl.add_widget(lab[0])
        bl.add_widget(gh2)
        return df

if __name__ == '__main__':
    app = TestApp()
    app.run()
