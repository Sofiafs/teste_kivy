from kivy.app import App
from kivy.uix.button import Button
from kivy.utils import get_color_from_hex

class MinhaApp(App):
    def build(self):
        return Button (text= "Clique aqui",font_size=50,background_color=get_color_from_hex('#0a0e2e')) 
if __name__ == '__main__':
    MinhaApp().run()

