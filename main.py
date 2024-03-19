from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from kivy.lang import Builder


class CalculatorLayout(BoxLayout):
    
    equation = StringProperty('')
    Builder.load_file("main.kv")    
    

    def press(self, button):
        
        if button == '=':
            try:
                self.equation = str(eval(self.equation))
                # self.equation = "Hello World "
            except Exception as e:
                self.equation = 'Error'
        elif button == 'C':
            self.equation = ''
        else:
            self.equation += button
            

class CalculatorApp(App):
    def build(self):
        return CalculatorLayout()


if __name__ == '__main__':
    CalculatorApp().run()